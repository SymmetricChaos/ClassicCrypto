# http://www.jfbouch.fr/crypto/m209/WORK/mathematical.html
# http://www.jfbouch.fr/crypto/m209/WORK/computer.html

from Ciphers.UtilityFunctions import printColumns

# The M209 was, in sense, one of the simplest of the cipher machines as it was
# operated entirely mechanically. However the machine settings were extremely
# elaborate.

# Translate the nice looking +-+-+ string into a list of 0s and 1s
def transPins(P):
    out = []
    for pins in P:
        out.append( [0 if i == "-" else 1 for i in pins] )
    return out

# Convert the friend [x,y] lug settings into binary lists
def lugPos(L):
    lugs = []
    for l in L:
        x = [0,0,0,0,0,0]
        for i in l:
            if i != 0:
                x[i-1] = 1
        lugs.append(x)
    return lugs

# Count up the lugs in each wheel position keeping in mind that 0 is in effective
# and that Python arrays start at zero.
def countLugs(L):
    count = [0,0,0,0,0,0]
    for l in L:
        for pos in l:
            if pos != 0:
                count[pos-1] += 1
    return count

#def activePins(P):
#    out = []
#    for pinList in P:
#        s = []
#        for pos,pin in enumerate(pinList):
#            if pin == "+":
#                s.append(pos)
#        out.append(s)
#    return out

def ltr2num(K):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    for i in K:
        out.append( alpha.index(i) )
    return out

def num2ltr(K):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    for i in K:
        out.append( alpha[i] )
    return out

def overlaps(lugs,lugp):
    overlaps = {}
    numOverlap = 0
    
    for bar in range(27):
        ctr = 0
        for wheel in range(6):
            if lugp[bar][wheel]:
               ctr += 1
    
        if ctr > 1:
            numOverlap += 1
            indx = ""
            for wheel in range(6):
                if lugp[bar][wheel]:
                    indx += str(wheel)
            if indx in overlaps:
                overlaps[indx] += 1 
            else:
                overlaps[indx] = 1 
    return overlaps

def M209(text,key,decode=False):
    
    text = ltr2num(text)
    indi = ltr2num(key[0])
    pins = transPins(key[1])
    acpins = activePins(key[1])
    lugs = countLugs(key[2])
    lugp = lugPos(key[2])
    over = overlaps(lugs,lugp)
    
    #   for i in setting:
    #        print(i)
    #   print()
    
    R1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    R2 = "ABCDEFGHIJKLMNOPQRSTUVXYZ" 
    R3 = "ABCDEFGHIJKLMNOPQRSTUVX"
    R4 = "ABCDEFGHIJKLMNOPQRSTU"
    R5 = "ABCDEFGHIJKLMNOPQRS"
    R6 = "ABCDEFGHIJKLMNOPQ"
    
    wheelLen = [26,25,23,21,19,17]
    sh = [15,14,13,12,11,10]
    
    
    pins[0] = [1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0]
    pins[1] = [1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0]
    pins[2] = [1,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1]
    pins[3] = [0,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1]
    pins[4] = [0,1,0,1,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1]
    pins[5] = [1,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1]
    
    lugs[0] = 2
    lugs[1] = 12
    lugs[2] = 1
    lugs[3] = 5
    lugs[4] = 10
    lugs[5] = 3
    
    lugp = [[0,0,1,0,0,1], [0,1,0,0,0,0], [0,1,0,0,0,0],
            [0,0,0,0,0,1], [0,1,0,0,0,0], [0,1,0,0,1,0],
            [1,0,0,0,0,1], [0,1,0,0,0,0], [0,1,0,0,1,0],
            [1,0,0,0,1,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,1,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            ]
    
    over = overlaps(lugs,lugp)
    print(over)
    
    L = []
    out = []
    for k,letter in enumerate(text):
        s = 0
        for w in range(6):
            #print(sh[w],indi[w],k,lugs[w])
            s += pins[w][ (sh[w] + indi[w] + k) % wheelLen[w]] * lugs[w]
        
        L.append((letter+s)%26)
        #print()
        #print()

    #printColumns(L,10,4)
    
    print(num2ltr(L))
    
def M209Example():
    
    import random
    random.seed(1)
    # Pins can be in either effective + or ineffective - positions
    pins = []
    for p in [26,25,23,21,19,17]:
         pins.append(random.choices("-+",k=p))
    
    for i in pins:
        print("".join(i))
    
    # There are 27 pairs of lugs 
    # They can be in one of six effective positions or in one of two ineffective
    # positions. Both lugs can be ineffective but both cannot be assigned to the
    # save effective position.
    # REMEMBER PYTHON ARRAYS START AT ZERO BUT M209 SPECIFICATION STARTS AT 1
    lugs = []
    for l in range(27):
        
        lugs.append(random.sample([0,0,1,2,3,4,5,6],k=2))
    
    printColumns(lugs,6)
    
    M209("THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",["PEOPLE",pins,lugs])
    
M209Example()
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

# Convert the friendly [a,b] lug settings into binary lists
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


def keystream(textlen,Lugs,Wheels,Pins,activePins):
    for i in range(textlen):
        K = 0
        for aBar in range(len(Lugs)):
            aBarShifted = False
            for wheel in range(len(Wheels)):
                if Pins[wheel][activePins[wheel] % len(Pins[wheel])] * Lugs[aBar][wheel]:
                    aBarShifted = True
            if aBarShifted:
                K += 1
        yield K
        for wheel in range(len(Wheels)):
            activePins[wheel] += 1

# Use pins and overlaps to calculate total overlaps
def totaloverlaps(O,P,i):
    total = [
            P[0][i%26]*P[1][i%25]*O['01'],
            P[0][i%26]*P[2][i%23]*O['02'],
            P[0][i%26]*P[3][i%21]*O['03'],
            P[0][i%26]*P[4][i%19]*O['04'],
            P[0][i%26]*P[5][i%17]*O['05'],
            P[1][i%25]*P[2][i%23]*O['12'],
            P[1][i%25]*P[3][i%21]*O['13'],
            P[1][i%25]*P[4][i%19]*O['14'],
            P[1][i%25]*P[5][i%17]*O['15'],
            P[2][i%23]*P[3][i%21]*O['23'],
            P[2][i%23]*P[4][i%19]*O['24'],
            P[2][i%23]*P[5][i%17]*O['25'],
            P[3][i%21]*P[4][i%19]*O['34'],
            P[3][i%21]*P[5][i%17]*O['35'],
            P[4][i%19]*P[5][i%17]*O['45']
            ]

    return sum(total)
    

def M209(text,key,decode=False):
    
    text = ltr2num(text)
    pins = transPins(key[1])
    LugsByWheel = countLugs(key[2])
    Lugs = lugPos(key[2])
    
    #   for i in setting:
    #        print(i)
    #   print()
    
    Wheels = [
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ABCDEFGHIJKLMNOPQRSTUVXYZ",
        "ABCDEFGHIJKLMNOPQRSTUVX",
        "ABCDEFGHIJKLMNOPQRSTU",
        "ABCDEFGHIJKLMNOPQRS",
        "ABCDEFGHIJKLMNOPQ"]
    

    
    sh = [15,14,13,12,11,10]

    pins[0] = [1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0]
    pins[1] = [1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0]
    pins[2] = [1,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1]
    pins[3] = [0,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1]
    pins[4] = [0,1,0,1,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1]
    pins[5] = [1,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1]
    
    
    LugsByWheel[0] = 2
    LugsByWheel[1] = 12
    LugsByWheel[2] = 1
    LugsByWheel[3] = 5
    LugsByWheel[4] = 10
    LugsByWheel[5] = 3
    
    Lugs = [[0,0,1,0,0,1], [0,1,0,0,0,0], [0,1,0,0,0,0],
            [0,0,0,0,0,1], [0,1,0,0,0,0], [0,1,0,0,1,0],
            [1,0,0,0,0,1], [0,1,0,0,0,0], [0,1,0,0,1,0],
            [1,0,0,0,1,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,1,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            [0,0,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0],
            ]
    
    # For each wheel add up the shift of the wheel and the position of the key
    # letter that is on it.
    activePins = [0,0,0,0,0,0]
    for wheel in range(len(Wheels)):
        activePins[wheel] = sh[wheel] + Wheels[wheel].index(key[0][wheel])
    
    K = keystream(len(text),Lugs,Wheels,pins,activePins)
    
    L = []
    for ltr,k in zip(text,K):

        s = ((25+k) - ltr) % 26
            
        L.append(s)
    
    return "".join( num2ltr(L) )
    
def M209Example():
    
    import random
    random.seed(1)
    # Pins can be in either effective + or ineffective - positions
    pins = []
    for p in [26,25,23,21,19,17]:
         pins.append(random.choices("-+",k=p))
    
    #for i in pins:
    #    print("".join(i))
    
    # There are 27 pairs of lugs 
    # They can be in one of six effective positions or in one of two ineffective
    # positions. Both lugs can be ineffective but both cannot be assigned to the
    # save effective position.
    # REMEMBER PYTHON ARRAYS START AT ZERO BUT M209 SPECIFICATION STARTS AT 1
    lugs = []
    for l in range(27):
        
        lugs.append(random.sample([0,0,1,2,3,4,5,6],k=2))
    
    #printColumns(lugs,6)
    
    ptext = "ATTACKZATZDAWN"
    ctext = M209(ptext,["PEOPLE",pins,lugs])
    dtext = M209(ctext,["PEOPLE",pins,lugs])
    print(ptext)
    print(ctext)
    print(dtext)
    
    
M209Example()

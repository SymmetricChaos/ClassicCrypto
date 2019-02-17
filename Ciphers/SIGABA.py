#http://ucsb.curby.net/broadcast/thesis/thesis.pdf

# Pass a singal through a rotor
def rotorC(letter,key,pos,invert=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    entry = alpha.index(letter)
    
    if invert == False:
        inner = key[(entry+pos-1)%26]
        outer = (alpha.index(inner)-pos+1)%26
        return alpha[outer]
    if invert == True:
        inner = alpha[(entry+pos-1)%26]
        outer = (key.index(inner)-pos+1)%26
        return alpha[outer]

def rotorI(letter,key,pos,invert=False):
    alpha = "0123456789"
    entry = alpha.index(letter)
    
    if invert == False:
        inner = key[(entry+pos-1)%10]
        outer = (alpha.index(inner)-pos+1)%10
        return alpha[outer]
    if invert == True:
        inner = alpha[(entry+pos-1)%10]
        outer = (key.index(inner)-pos+1)%10
        return alpha[outer]
    
# Simulator of a SIGABA like machine
# Need to find a way to confirm behavior
def SIGABA(text,keys,decode=False):
    
    # Settings for each of the rotor groups
    cipherRotorsSet = keys[0]
    controlRotorsSet = keys[1]
    indexRotorsSet = keys[2]
    
    cipherPos = keys[3]
    controlPos = keys[4]
    indexPos = keys[5]
    
    # Rotor configurations were randomly generated.
    # Need to learn what actual configurations were or how they were chosen

    largeRotors = {"I": "PWJVDRGTMBHOLYXUZFQEAINKCS",
                   "II": "MKLWAIBXRUYGTNCSPDFQHZJVOE",
                   "III": "WVYLIJAMXZTSUROENDKQHCFBPG",
                   "IV": "ZRMQWNITBJUKHOFPEYDXAVLSGC",
                   "V": "LGBAZWMIPQTFHEVUYJNCRSKDOX",
                   "VI": "YGOWZXPCBJTIARKHMELNDFVUSQ",
                   "VII": "UZGKPDQRJTFCYOINVMALHEXWSB",
                   "VIII": "OQRTDBUZGPHWNJFELKCIXVSAYM",
                   "IX": "HLEDCOTJMUAWFZQIGRBVYPSNKX",
                   "X": "QKCIYPWLZNHTJVFDURSXEBGMOA"}
    
    smallRotors = {"I": "9438705162",
                   "II": "8135624097",
                   "III": "5901284736",
                   "IV": "1953742680",
                   "V": "6482359170"}
    
    cipherRotors = []
    for num in cipherRotorsSet:
        cipherRotors.append(largeRotors[num])
    
    controlRotors = []
    for num in controlRotorsSet:
        controlRotors.append(largeRotors[num])
    
    indexRotors = []
    for num in indexRotorsSet:
        indexRotors.append(smallRotors[num])
    
    # Wiring that connects the control rotors to the index rotors
    indwiring = {"A": 9, "B": 1, "C": 2, "D": 3, "E": 3, "F": 4,
                 "G": 4, "H": 4, "I": 5, "J": 5, "K": 5, "L": 6,
                 "M": 6, "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7,
                 "S": 7, "T": 7, "U": 8, "V": 8, "W": 8, "X": 8,
                 "Y": 8, "Z": 8}
    
    out = []
    for ctr,letter in enumerate(text,1):
        # Encrypt the letter
        T = letter
        for R,P in zip(cipherRotors,cipherPos):
            T = rotorC(T,R,P)
        out.append(T)
        
        # Put A, B, C, and D through the control rotors
        L = ["A","B","C","D"]
        for R,P in zip(controlRotors,controlPos):
            L[0] = rotorC(L[0],R,P)
            L[1] = rotorC(L[1],R,P)
            L[2] = rotorC(L[2],R,P)
            L[3] = rotorC(L[3],R,P)

        # Group the results of the step maze for input to the index rotors
        # There will be some duplicates here. That's okay we'll remove them later
        for i in range(4):
            L[i] = str(indwiring[L[i]])
        
        # Send the grouped wires into the index rotors
        for R,P in zip(indexRotors,indexPos):
            L[0] = rotorI(L[0],R,P)
            L[1] = rotorI(L[1],R,P)
            L[2] = rotorI(L[2],R,P)
            L[3] = rotorI(L[3],R,P)
        
        # Advance the control rotors
        controlPos[2] = (controlPos[2] + 1) % 26
        if ctr % 26 == 0:
            controlPos[3] = (controlPos[3] + 1) % 26
        if ctr % 676 == 0:
            controlPos[1] = (controlPos[1] + 1) % 26     
        
        # Now determine which cipher rotors should move
        # To do this first we use floored division to make pairs out of 0 and 1, 2 and 3, 4 and 5, and so on
        L = [(int(i))//2 for i in L]
        # We for the list into a set to ensure there are no duplicates
        for rtr in set(L):
            cipherPos[rtr] = (cipherPos[rtr] + 1) % 26

        
    return "".join(out)

def SIGABAExample():

    cipher = ["V","I","II","IV","II"]
    control = ["IX","VI","X","VII","VIII"]
    index = ["II","I","V","IV","III"]
    cipherPos = [5,17,11,23,3]
    controlPos = [5,17,11,23,3]
    indexPos = [5,17,11,23,3]
    
    ptext = "IAMTHEVERYMODELOFAMODERNMAJORGENERAL"
    
    ctext = SIGABA(ptext,[cipher,control,index,cipherPos,controlPos,indexPos])
    
    print(ptext)
    print(ctext)
    
#SIGABAExample()
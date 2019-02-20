#http://ucsb.curby.net/broadcast/thesis/thesis.pdf



# Pass a signal through a Cipher or Control rotors
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

# Pass a signal through an index rotor   
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
    cipherRotorsSet = keys[0].copy()
    controlRotorsSet = keys[1].copy()
    indexRotorsSet = keys[2].copy()
    
    indicator1 = keys[3]
    indicator2 = keys[4]
    indicator3 = keys[5]
        
    # Rotor Wirings for the large rotors
    # The actual wirings are apparently still classified.
    largeRotors = {"I":    "PWJVDRGTMBHOLYXUZFQEAINKCS",
                   "II":   "MKLWAIBXRUYGTNCSPDFQHZJVOE",
                   "III":  "WVYLIJAMXZTSUROENDKQHCFBPG",
                   "IV":   "ZRMQWNITBJUKHOFPEYDXAVLSGC",
                   "V":    "LGBAZWMIPQTFHEVUYJNCRSKDOX",
                   "VI":   "YGOWZXPCBJTIARKHMELNDFVUSQ",
                   "VII":  "UZGKPDQRJTFCYOINVMALHEXWSB",
                   "VIII": "OQRTDBUZGPHWNJFELKCIXVSAYM",
                   "IX":   "HLEDCOTJMUAWFZQIGRBVYPSNKX",
                   "X":    "QKCIYPWLZNHTJVFDURSXEBGMOA"}
    
    # Rotor Wirings for the small rotors
    # The actual wirings are apparently still classified.
    smallRotors = {"I":   "9438705162",
                   "II":  "8135624097",
                   "III": "5901284736",
                   "IV":  "1953742680",
                   "V":   "6482359170"}
    
    cipherRotors = []
    cipherPos = []
    for ctr,num in enumerate(cipherRotorsSet):
        cipherRotors.append(largeRotors[num])
        cipherPos.append(largeRotors[num].index(indicator1[ctr]))
    
    # If we are decoding then keep a list with the rotors in reverse
    if decode == True:
        cipherRotorsRev = cipherRotors[::-1]
    
    controlRotors = []
    controlPos = []
    for num in controlRotorsSet:
        controlRotors.append(largeRotors[num])
        controlPos.append(largeRotors[num].index(indicator2[ctr]))
    
    indexRotors = []
    indexPos = []
    for num in indexRotorsSet:
        indexRotors.append(smallRotors[num])
        indexPos.append(smallRotors[num].index(indicator3[ctr]))
    
    
    # Wiring that connects the control rotors to the index rotors
    indwiring = {"A": 9, "B": 1, "C": 2, "D": 3, "E": 3, "F": 4,
                 "G": 4, "H": 4, "I": 5, "J": 5, "K": 5, "L": 6,
                 "M": 6, "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7,
                 "S": 7, "T": 7, "U": 8, "V": 8, "W": 8, "X": 8,
                 "Y": 8, "Z": 8}
    
    out = []
    for ctr,letter in enumerate(text,1):
        
        # Encrypt the letter
        if decode == False:
            T = letter
            for R,P in zip(cipherRotors,cipherPos):
                T = rotorC(T,R,P)
            out.append(T)
        
        if decode == True:
            # We need to pass the signal through the cipher rotors in reverse
            # when we are decrypting. The order of the rotor was reversed earlier
            # but we need to invert the cipher positions each time since positions
            # are constantly being changed.
            cipherPosRev = cipherPos[::-1]
            T = letter
            for R,P in zip(cipherRotorsRev,cipherPosRev):
                T = rotorC(T,R,P,invert=True)
            out.append(T)
        
        # Put A, B, C, and D through the control rotors, this is called the "step maze"
        L = ["A","B","C","D"]
        for R,P in zip(controlRotors,controlPos):
            L[0] = rotorC(L[0],R,P)
            L[1] = rotorC(L[1],R,P)
            L[2] = rotorC(L[2],R,P)
            L[3] = rotorC(L[3],R,P)
            
        # Now advance the control rotors
        # (Unsure if this is the exact scheme used but it is simple and matches
        #  what is described in documentation I can find)
        controlPos[2] = (controlPos[2] + 1) % 26
        if ctr % 26 == 0:
            controlPos[3] = (controlPos[3] + 1) % 26
        if ctr % 676 == 0:
            controlPos[1] = (controlPos[1] + 1) % 26     

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
        
        # The outputs of the index rotors determine which of the cipher rotors
        # will move. We used floored vision to pair up each the sen signals.
        L = [(int(i))//2 for i in L]
        # We for the list into a set to ensure there are no duplicates
        for rtr in set(L):
            cipherPos[rtr] = (cipherPos[rtr] + 1) % 26

        
    return "".join(out)

def SIGABAExample():

    cipher =     ["V","IX","II","IV","III"]
    control =    ["IX","VI","I","VII","VIII"]
    index =      ["II","I","V","IV","III"]
    indicator =  "TABLE"
    controlPos = "GRAPH"
    indexPos =   "02367"
    
    ptext = "IAMTHEVERYMODELOFAMODERNMAJORGENERAL"
    
    ctext = SIGABA(ptext,[cipher,control,index,indicator,controlPos,indexPos],
                   decode=False)
    dtext = SIGABA(ctext,[cipher,control,index,indicator,controlPos,indexPos],
                   decode=True)
        
    print(ptext)
    print(ctext)
    print(dtext)
    
#SIGABAExample()
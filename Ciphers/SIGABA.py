#http://ucsb.curby.net/broadcast/thesis/thesis.pdf

# Pass a singal through a rotor
def rotor(letter,key,pos,invert=False):
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
    
# Should get around to a copy of Enigma at some point
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
    cipherRotors = []
    for num in cipherRotorsSet:
        if num == "I":
            cipherRotors.append("PWJVDRGTMBHOLYXUZFQEAINKCS")
        if num == "II":
            cipherRotors.append("MKLWAIBXRUYGTNCSPDFQHZJVOE")
        if num == "III":
            cipherRotors.append("WVYLIJAMXZTSUROENDKQHCFBPG")
        if num == "IV":
            cipherRotors.append("ZRMQWNITBJUKHOFPEYDXAVLSGC")
        if num == "V":
            cipherRotors.append("LGBAZWMIPQTFHEVUYJNCRSKDOX")
    
    controlRotors = []
    for num in controlRotorsSet:
        if num == "I":
            controlRotors.append("YGOWZXPCBJTIARKHMELNDFVUSQ")
        if num == "II":
            controlRotors.append("UZGKPDQRJTFCYOINVMALHEXWSB")
        if num == "III":
            controlRotors.append("OQRTDBUZGPHWNJFELKCIXVSAYM")
        if num == "IV":
            controlRotors.append("HLEDCOTJMUAWFZQIGRBVYPSNKX")
        if num == "V":
            controlRotors.append("QKCIYPWLZNHTJVFDURSXEBGMOA")
    
    indexRotors = []
    for num in indexRotorsSet:
        if num == "I":
            indexRotors.append("9438705162")
        if num == "II":
            indexRotors.append("8135624097")
        if num == "III":
            indexRotors.append("5901284736")
        if num == "IV":
            indexRotors.append("1953742680")
        if num == "V":
            indexRotors.append("6482359170")
    
    indwiring = {"A": 9, "B": 1, "C": 2, "D": 3, "E": 3, "F": 4,
                 "G": 4, "H": 4, "I": 5, "J": 5, "K": 5, "L": 6,
                 "M": 6, "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7,
                 "S": 7, "T": 7, "U": 8, "V": 8, "W": 8, "X": 8,
                 "Y": 8, "Z": 8}
    
    out = []
    for letter in text:
        # Encrypt the letter
        T = letter
        for R,P in zip(cipherRotors,cipherPos):
            T = rotor(T,R,P)
        out.append(T)
        
        # Put A, B, C, and D through the control rotors
        L = ["A","B","C","D"]
        for R,P in zip(controlRotors,controlPos):
            L[0] = rotor(L[0],R,P)
            L[1] = rotor(L[1],R,P)
            L[2] = rotor(L[2],R,P)
            L[3] = rotor(L[3],R,P)

        # Group the results of the step maze for input to the index rotors
        for i in range(4):
            L[i] = indwiring[L[i]]
    
        for R,P in zip(indexRotors,indexPos):
            pass
            
    
    return "".join(out)

cipher = ["V","I","II","IV","II"]
control = ["V","I","II","IV","II"]
index = ["V","I","II","IV","II"]
cipherPos = [5,17,11,23,3]
controlPos = [5,17,11,23,3]
indexPos = [5,17,11,23,3]

ptext = "THEQUICKBROWNFOX"

ctext = SIGABA(ptext,[cipher,control,index,cipherPos,controlPos,indexPos])

print(ctext)
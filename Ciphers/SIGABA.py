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
    
    

from Ciphers.UtilityFunctions import alphaToNumber, numberToAlpha

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

# Generate the keystream
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



def M209(text,key,decode=False):
    
    # We need the wheels to check for possible errors
    Wheels = [
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ABCDEFGHIJKLMNOPQRSTUVXYZ",
        "ABCDEFGHIJKLMNOPQRSTUVX",
        "ABCDEFGHIJKLMNOPQRSTU",
        "ABCDEFGHIJKLMNOPQRS",
        "ABCDEFGHIJKLMNOPQ"]
    
    # Wrong number of letters
    if len(key[0]) != 6:
        raise Exception("Key must have exactly six letters")
    
    # Check if valid letters were used in the key
    for i in range(6):
        if key[0][i] not in Wheels[i]:
            raise Exception("Wheel {} can only have letters in {}".format(i+1,Wheels[i]))


    text = alphaToNumber(text)
    pins = transPins(key[1])
    Lugs = lugPos(key[2])

    sh = [15,14,13,12,11,10]

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
    
    return "".join( numberToAlpha(L) )
    

from itertools import product
from UtilityFunctions import alphabetPermutation

# The polybius square is a way of converting each letter of an alphabet into a
# a pair of numbers. In order for this to work the size of the alphabet should
# be close to a square number. There are three commons ways to do this. 
# Replace the uncommon letter J with the common letter I that looks similar.
# Replace the letter C with the letter K which is pronounced similarly. 
# Extend the alphabet with the ten digits.
# This cipher uses the extended alphabet as the default.

# Technically the polybiusSquare is just a simple substitution cipher. However
# it is extremely useful in other ciphers.

# The "sep" keyword allows the symbol that separates the codegroups of the
# polybius square. By default there is no separation at all. This setting is
# useful for better readbility or the nihilist cipher.

def polybiusSquare(text,key="",decode=False,mode="EX",sep=""):
    #the IJ version of the polybius (25 characters)
    if mode == "IJ":
        alpha = "ABCEDFGHIKLMNOPQRSTUVWXYZ"
        text = text.replace("J","I")
        key = key.replace("J","I")

    #the CK version of the polybius (25 characters)
    if mode == "CK":
        alpha = "ABEDFGHIJKLMNOPQRSTUVWXYZ"
        text = text.replace("C","K")
        key = key.replace("C","K")
        
    #the extended version of the polybius (36 characters)
    if mode == "EX":
        alpha = "ABCEDFGHIJKLMNOPQRSTUVWXYZ0123456789"

    
    # Generate the internal key using user key
    k = alphabetPermutation(key,alphabet=alpha)

    if mode == "EX":
        codegroups = ["".join(i) for i in product("123456",repeat=2)]
    else:
        codegroups = ["".join(i) for i in product("12345",repeat=2)]
        

    if decode == False:
        # Pair each letter with a codegroup
        D = {}
        for i,j in zip(k,codegroups):
            D[i] = j
        
        ctext = [D[let] for let in text]
    
        return sep.join(ctext)
    
    if decode == True:
        # Pair each codegrou with a letter
        D = {}
        for i,j in zip(k,codegroups):
            D[j] = i
        if sep != "":
            grps = text.split(sep)
        else:
            grps = [text[2*j:2*j+2] for j in range(len(text)//2)]
        dtext = [D[pair] for pair in grps]
    
        return "".join(dtext)

def polybiusSquareExample():
    ptext = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
    key = "FIVEZEBRAS"
    print("Example Of A Polybius Square\n\nKey is {}\n".format(key))
    
    print("Plaintext is:  {}\n\n".format(ptext))
    
    for mode in ["IJ","CK","EX"]:
        print("Using Mode {}".format(mode))
        ctext = polybiusSquare(ptext,key,mode=mode,sep=" ")
        print("Ciphertext is: {}".format(ctext))
        dtext = polybiusSquare(ctext,key,decode=True,mode=mode,sep=" ")
        print("Decodes As:    {}".format(dtext))
        print()

#polybiusSquareExample()
from itertools import product

# The polybius square is a way of converting each letter of an alphabet into a
# a pair of numbers. In order for this to work the size of the alphabet should
# be close to a square number. There are three commons ways to do this. 
# Replace the uncommon letter J with the common letter I that looks similar.
# Replace the letter C with the letter K which is pronounced similarly. 
# Extend the alphabet with the ten digits.
# This cipher uses the extended alphabet as the default.

# Technically the polybiusSquare is just a simple substitution cipher. However
# it is extremely useful in other ciphers.

def polybiusSquare(text,key="",decode=False,mode="EX"):
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
    k = ""
    for letter in key:
        if letter not in k:
            k += letter
    for letter in alpha:
        if letter not in k:
            k += letter

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
    
        return "".join(ctext)
    
    if decode == True:
        # Pair each codegrou with a letter
        D = {}
        for i,j in zip(k,codegroups):
            D[j] = i
        
        pairs = [text[2*j:2*j+2] for j in range(len(text)//2)]
        dtext = [D[pair] for pair in pairs]
    
        return "".join(dtext)
         
#ptext = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"

#for mode in ["IJ","CK","EX"]:
#    ctext = polybiusSquare(ptext,"FIVEZEBRAS",mode=mode)
#    print(ctext)
#    dtext = polybiusSquare(ctext,"FIVEZEBRAS",decode=True,mode=mode)
#    print(dtext)
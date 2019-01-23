from Ciphers.UtilityFunctions import groups, alphabetPermutation
import numpy as np

def twoSquare(text,keys,decode=False,printkey=False):
        
    k1 = alphabetPermutation(keys[0],"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    k2 = alphabetPermutation(keys[1],"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    sq1 = np.full([6,6],"")
    sq2 = np.full([6,6],"")
    alphasq = np.full([6,6],"")
    for i in range(6):
        sq1[i] = [x for x in groups(k1,6)[i]]
        sq2[i] = [x for x in groups(k2,6)[i]]
        alphasq[i] = [x for x in groups("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",6)[i]]

    if printkey == True:
        for i in range(6):
            print(" ".join(sq1[i]))
        print()
        for i in range(6):
            print(" ".join(sq2[i]),end="  ")
        return ""


    if len(text) % 2 == 1:
        text += "X"
    G = groups(text,2)
    
    
    if decode == False:
        out = ""
        for g in G:
            # MAKE IT DO THE STUFF
            pass

    
    if decode == True:
        out = ""
        for g in G:
            # MAKE IT DO THE OTHER STUFF
            pass

    
def twoSquareExample():
    print("Example of the Four Square Cipher\n")
    print("The key is:")
    keys = ["953SQUARE178","621CIPHER457"]
    fourSquare("TEST",keys,printkey=True)
    
    print("")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = twoSquare(ptext,["753SQUARE198","621CIPHER457"])
    dtext = twoSquare(ctext,["753SQUARE198","621CIPHER457"],decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
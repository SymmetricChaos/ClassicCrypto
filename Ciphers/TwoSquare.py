import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.UtilityFunctions import groups, alphabetPermutation
import numpy as np

def twoSquare(text,keys,decode=False,printkey=False):
        
    k1 = alphabetPermutation(keys[0],"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    k2 = alphabetPermutation(keys[1],"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    sq1 = np.full([6,6],"")
    sq2 = np.full([6,6],"")
    for i in range(6):
        sq1[i] = [x for x in groups(k1,6)[i]]
        sq2[i] = [x for x in groups(k2,6)[i]]

    if printkey == True:
        for i in range(6):
            print(" ".join(sq1[i]))
        print()
        for i in range(6):
            print(" ".join(sq2[i]))
        return ""


    if len(text) % 2 == 1:
        text += "X"
    G = groups(text,2)
    
    
    # The two square cipher is involutive which means that encryption is
    # exactly the same as decryption. The decode argument is ignored but must
    # exist for compatibility.
    out = ""
    for g in G:
        A = np.where(sq1 == g[0])
        B = np.where(sq2 == g[1])
                
        out += sq1[A[0],B[1]][0]
        out += sq2[B[0],A[1]][0]
            
    return out

    
def twoSquareExample():
    print("Example of the Two Square Cipher\n")
    print("The key is:")
    keys = ["953SQUARE178","621CIPHER457"]
    twoSquare("",keys,printkey=True)
    
    print("")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = twoSquare(ptext,["753SQUARE198","621CIPHER457"])
    dtext = twoSquare(ctext,["753SQUARE198","621CIPHER457"],decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#twoSquareExample()
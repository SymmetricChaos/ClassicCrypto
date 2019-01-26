import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.UtilityFunctions import groups, makeSquare
import numpy as np

def twoSquare(text,keys,decode=False,mode="EX",printkey=False):
    
    # Convert the squares to numpy arrays to we can use numpy's indexing
    sq1 = np.array(makeSquare(keys[0],mode))
    sq2 = np.array(makeSquare(keys[1],mode))
    
    if mode == "IJ" or mode == "JI":
        text = text.replace("J","I")
    if mode == "KQ" or mode == "QK":
        text = text.replace("Q","K")
    if mode == "CK" or mode == "KC":
        text = text.replace("C","K")
        
    if len(text) % 2 == 1:
        text += "X"

    
    # Print out the key in a nice way if the user needs it
    if printkey == True:
        if mode == "EX":
            for i in range(6):
                print(" ".join(sq1[i]))
            print()
            for i in range(6):
                print(" ".join(sq2[i]))
        else:
            for i in range(5):
                print(" ".join(sq1[i]))
            print()
            for i in range(5):
                print(" ".join(sq2[i]))

    if mode == "EX":
        sz = 6
    else:
        sz = 5
    
    G = groups(text,2)
    
    if decode == False:
        out = ""
        for g in G:
            A = np.where(sq1 == g[0])
            B = np.where(sq2 == g[1])

            
            if A[0] == B[0]:
                out += sq1[(A[0]+1)%sz,A[1]][0]
                out += sq2[(B[0]+1)%sz,B[1]][0]
                
            elif A[1] == B[1]:
                out += sq1[A[0],(A[1]+1)%sz][0]
                out += sq2[B[0],(B[1]+1)%sz][0]
                
            else:
                out += sq1[A[0],B[1]][0]
                out += sq2[B[0],A[1]][0]
            
            
    if decode == True:
        out = ""
        for g in G:
            A = np.where(sq1 == g[0])
            B = np.where(sq2 == g[1])
            
            if A[0] == B[0]:
                out += sq1[(A[0]-1)%sz,A[1]][0]
                out += sq2[(B[0]-1)%sz,B[1]][0]
                
            elif A[1] == B[1]:
                out += sq1[A[0],(A[1]-1)%sz][0]
                out += sq2[B[0],(B[1]-1)%sz][0]
                
            else:
                out += sq1[A[0],B[1]][0]
                out += sq2[B[0],A[1]][0]
    return out

    
def twoSquareExample():
    print("Example of the Two Square Cipher\n")
    print("The key is:")
    keys = ["TWOSQUARE","CIPHER"]
    twoSquare("",keys,printkey=True,mode="IJ")
    
    print("")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = twoSquare(ptext,keys,mode="IJ")
    dtext = twoSquare(ctext,keys,decode=True,mode="IJ")
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#twoSquareExample()
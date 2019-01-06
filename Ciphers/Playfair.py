from UtilityFunctions import groups, alphabetPermutation
import numpy as np
from PrepareText import playfairPrep

            

def playfairCipher(text,key,decode=False,mode="IJ",printkey=False):
    
    # Make sure the text will work correctly for a playfair cipher in this mode
    text = playfairPrep(text,mode=mode)
    
    # Derive the alphabet to be used for the key based on the mode
    if mode == "IJ" or mode == "JI":
        key = key.replace("J","I")
        k = alphabetPermutation(key,"ABCDEFGHIKLMNOPQRSTUVWXYZ")
    if mode == "CK" or mode == "KC":
        key = key.replace("C","K")
        k = alphabetPermutation(key,"ABDEFGHIJKLMNOPQRSTUVWXYZ")
    if mode == "KQ" or mode == "QK":
        key = key.replace("Q","K")
        k = alphabetPermutation(key,"ABCDEFGHIJKLMNOPRSTUVWXYZ")
    if mode == "EX":
        k = alphabetPermutation(key,"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    
    if mode == "EX":
        sq = np.full([6,6],"")
        for i in range(6):
            sq[i] = [x for x in groups(k,6)[i]]
    
        if printkey == True:
            for i in range(6):
                print(" ".join(sq[i]))
            return ""
        
    else:
        sq = np.full([5,5],"")
        for i in range(5):
            sq[i] = [x for x in groups(k,5)[i]]
    
        if printkey == True:
            for i in range(5):
                print(" ".join(sq[i]))
            return ""
    
    G = groups(text,2)

    if decode == False:
        if mode == "EX":
            sz = 6
        else:
            sz = 5
    
        out = ""
        
        for g in G:
            A = np.where(sq == g[0])
            B = np.where(sq == g[1])
            #print(g)
            
            if A[0] == B[0]:
                out += sq[(A[0]+1)%sz,A[1]][0]
                out += sq[(B[0]+1)%sz,B[1]][0]
                #print(out[-2:],"\n")
                
            elif A[1] == B[1]:
                out += sq[A[0],(A[1]+1)%sz][0]
                out += sq[B[0],(B[1]+1)%sz][0]
                #print(out[-2:],"\n")
                
            else:
                out += sq[A[0],B[1]][0]
                out += sq[B[0],A[1]][0]
                #print(out[-2:],"\n")
        
        return out
    
    if decode == True:
        if mode == "EX":
            sz = 6
        else:
            sz = 5
    
        out = ""
        
        for g in G:
            A = np.where(sq == g[0])
            B = np.where(sq == g[1])
            #print(g)
            
            if A[0] == B[0]:
                out += sq[(A[0]-1)%sz,A[1]][0]
                out += sq[(B[0]-1)%sz,B[1]][0]
                #print(out[-2:],"\n")
                
            elif A[1] == B[1]:
                out += sq[A[0],(A[1]-1)%sz][0]
                out += sq[B[0],(B[1]-1)%sz][0]
                #print(out[-2:],"\n")
                
            else:
                out += sq[A[0],B[1]][0]
                out += sq[B[0],A[1]][0]
                #print(out[-2:],"\n")
        
        return out
            




def fourSquareCipher(text,keys,decode=False,printkey=False):
    

    
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
            print(" ".join(alphasq[i]),end="  ")
            print(" ".join(sq1[i]))
        print()
        for i in range(6):
            print(" ".join(sq2[i]),end="  ")
            print(" ".join(alphasq[i]))
        return ""


    if len(text) % 2 == 1:
        text += "X"
    G = groups(text,2)
    
    if decode == False:
        out = ""
        for g in G:
            A = np.where(sq1 == g[0])
            B = np.where(sq2 == g[1])
            
            out += alphasq[A[0],B[1]][0]
            out += alphasq[B[0],A[1]][0]
            
        return out
    
    if decode == True:
        out = ""
        for g in G:
            A = np.where(alphasq == g[0])
            B = np.where(alphasq == g[1])
            
            out += sq1[A[0],B[1]][0]
            out += sq2[B[0],A[1]][0]
            
        return out

def fourSquareExample():
    print("Example of the Four Square Cipher\n")
    print("The key is:")
    keys = ["4SQUARE5","738CIPHER091"]
    fourSquareCipher("TEST",keys,printkey=True)
    
    print("")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = fourSquareCipher(ptext,["2SQUARE5","738CIPHER091"])
    dtext = fourSquareCipher(ctext,["2SQUARE5","738CIPHER091"],decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    

def playfairCipherExample():
    print("Example of the Playfair Cipher")

    
    for i in ["IJ","CK","KQ","EX"]:
        print("\n\nIn {} mode the key is:".format(i))
        key = "PLAYFAIR"
        playfairCipher("",key,mode=i,printkey=True)
        ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
        ctext = playfairCipher(ptext,"PLAYFAIR",mode=i)
        dtext = playfairCipher(ctext,"PLAYFAIR",decode=True,mode=i)
        print("\nPlaintext is:  {}".format(ptext))
        print("Ciphertext is: {}".format(ctext))
        print("Decodes As:    {}".format(dtext))
    
playfairCipherExample()
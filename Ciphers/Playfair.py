from Ciphers.UtilityFunctions import groups, alphabetPermutation
import numpy as np
from Ciphers.PrepareText import playfairPrep

            

def playfair(text,key,decode=False,mode="IJ",printkey=False):
    
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
    

def playfairExample():
    print("Example of the Playfair Cipher")

    
    for i in ["IJ","CK","KQ","EX"]:
        print("\n\nIn {} mode the key is:".format(i))
        key = "PLAYFAIR"
        playfair("",key,mode=i,printkey=True)
        ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
        ctext = playfair(ptext,"PLAYFAIR",mode=i)
        dtext = playfair(ctext,"PLAYFAIR",decode=True,mode=i)
        print("\nPlaintext is:  {}".format(ptext))
        print("Ciphertext is: {}".format(ctext))
        print("Decodes As:    {}".format(dtext))
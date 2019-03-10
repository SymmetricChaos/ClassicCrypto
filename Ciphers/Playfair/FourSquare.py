from Ciphers.UtilityFunctions import makeSquare, groups
import numpy as np

def fourSquare(text,keys,decode=False,mode="IJ",printkey=False):
        
    # Convert the squares to numpy arrays to we can use numpy's indexing
    sq1 = np.array(makeSquare(keys[0],mode=mode))
    sq2 = np.array(makeSquare(keys[1],mode=mode))
    alphasq = np.array(makeSquare("",mode=mode))
    
    if mode == "IJ" or mode == "JI":
        text = text.replace("J","I")
    if mode == "KQ" or mode == "QK":
        text = text.replace("Q","K")
    if mode == "CK" or mode == "KC":
        text = text.replace("C","K")
    
    if printkey == True:
        n = 5
        if mode == "EX":
            n = 6
        for i in range(n):
            print(" ".join(alphasq[i]),end="  ")
            print(" ".join(sq1[i]))
        print()
        for i in range(n):
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

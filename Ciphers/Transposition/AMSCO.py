# http://www.cryptogram.org/downloads/aca.info/ciphers/Amsco.pdf

from itertools import cycle
from Ciphers.UtilityFunctions import uniqueRank, groups
from numpy import argsort

def alternating(text,mode="odd"):
    T = list(text)
    L = []
    
    if mode == "odd":
        e = [1,2]
    if mode == "even":
        e = [2,1]
        
    for i in cycle(e):
    
        if len(T) == 0:
            break
        
        if i == 2 and len(T) > 1:
            L.append( T.pop(0) + T.pop(0) )
            
        else:
            L.append( T.pop(0) )
                
    return L

def AMSCO(text,key,decode=False,mode="odd"):
    
    # Derive the key
    k = uniqueRank(key)
    
    # Divide the text into alternating groups of 2 and 1
    L = alternating(text,mode=mode)
    
    x = groups(L,len(k))    

    if decode == False:
        
        out = []
        for col in argsort(k):
            for row in x:
                if len(row) > col:
                    out.append(row[col])
    
        return "".join(out)
    
    if decode == True:
        
        #for i in x:
        #    print(i)
        # In order to decode we need to figure out a bunch about the grid that
        # was used based on what the key is. We don't care what is in the grid
        # right now only how many letters are in each cell because this is the
        # same when encrypting and decrypting.
        
        # How many rows and columns
        numRow = len(x)
        numCol = len(k)
        
        # Put zero length string into the grid to make counting easier
        while len(x[-1]) < numCol:
            x[-1].append("")

        # Count up how many letters are in each column
        colLens = {}
        for i,s in zip(range(numCol),k):
            ctr = 0
            
            for j in range(numRow):
                ctr += len(x[j][i])

            if len(x[0][i]) == 2:
                n = "even"
            if len(x[0][i]) == 1:
                n = "odd"

            colLens[s] = [ctr,n]
        
        G = []
        ctr = 0
        for i in range(numCol):
            l,e = colLens[i]
            
            # If the key length is odd alternate the groupings
            if len(k) % 2 == 1:
                G.append( alternating(text[ctr:ctr+l],e) )
                ctr += l
            # Otherwise groups of 2 or groups of 1
            else:
                if e == "even":
                    G.append( groups(text[ctr:ctr+l],2) )
                if e == "odd":
                    G.append( groups(text[ctr:ctr+l],1) )
                ctr += l
        
        # These groups also need to be evened out in length with zero length
        # strings
        for i in G:
            if len(i) < numRow:
                i.append("")
        
        #print(numRow)
        #for i in G:
        #    print(len(i),end="  ")
        #    print(i)
        
        out = []
        for j in range(numRow):
            for i in k:
                out.append(G[i][j])
        
        return "".join(out)
        

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

def AMSCO(text,key,decode=False):
    
    # Derive the key
    k = uniqueRank(key)
    
    # Divide the text into alternating groups of 2 and 1
    L = alternating(text)
    
    x = groups(L,len(k))    

    if decode == False:
        
        for i in x:
            print(i)
    
        out = []
        for col in argsort(k):
            for row in x:
                if len(row) > col:
                    out.append(row[col])
    
        return "".join(out)
    
    if decode == True:
        
        
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
                if ctr == 2:
                    n = "even"
                if ctr == 1:
                    n = "odd"
            colLens[s] = [ctr,n]
            
        
        ctr = 0
        for i in range(numCol):
            l,e = colLens[i]
            print(alternating(text[ctr:ctr+l],e))
            ctr += l
        
        


ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
ptext = "INCOMPLETECOLUMNARWITHALTERNATINGSINGLELETTERSANDDIGRAPHS"
ctext = AMSCO(ptext,"13204")
print(ctext)
print()
dtext = AMSCO(ctext,"13204",decode=True)
print(dtext)
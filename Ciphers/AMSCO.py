# http://www.cryptogram.org/downloads/aca.info/ciphers/Amsco.pdf

from itertools import cycle
from Ciphers.UtilityFunctions import uniqueRank, groups
from numpy import argsort

def AMSCO(text,key,decode=False):
    
    # Derive the key
    k = uniqueRank(key)
    #print(k)

    # Convert the text to a list for easy maniplation
    T = list(text)
    L = []
    
    # Divide the text into alternating groups of 2 and 1
    if decode == False:
        e = [2,1]
    else:
        e = [1,2]
    for i in cycle(e):
        
        if len(T) == 0:
            break
        
        if i == 2 and len(T) > 1:
            L.append( T.pop(0) + T.pop(0) )
            
        else:
            L.append( T.pop(0) )
    
    x = groups(L,len(k))
    for i in x:
        print(i)
    
    # Determine which columns are long
    # Sometimes all columns are long but we correct for that by reducing the
    # number of rows by 1.
    longCols = [i for i in range(len(x[-1]))]
    numRow = len(x)-1
    numCol = len(k)
    
    if decode == False:
    
        out = []
        for col in argsort(k):
            for row in x:
                if len(row) > col:
                    out.append(row[col])
    
        return "".join(out)
    
    if decode == True:
        out = []
        for col in k:
            for row in x:
                if len(row) > col:
                    out.append(row[col])
    
        return "".join(out)


ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
ptext = "INCOMPLETECOLUMNARWITHALTERNATINGSINGLELETTERSANDDIGRAPHS"
ctext = AMSCO(ptext,"13204")
print(ctext)
dtext = AMSCO(ctext,"13204",decode=True)
print(dtext)
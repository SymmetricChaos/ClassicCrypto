# http://www.cryptogram.org/downloads/aca.info/ciphers/Amsco.pdf

from itertools import cycle
from Ciphers.UtilityFunctions import uniqueRank
import random
from numpy import argsort

def AMSCO(text,key,decode=False):
    
    k = uniqueRank(key)


    T = list(text)
    L = []
    
    for i in cycle([1,2]):
        
        if len(T) == 0:
            break
        
        if i == 2 and len(T) > 1:
            L.append( T.pop(0) + T.pop(0) )
            
        else:
            L.append( T.pop(0) )
    
    print(L)

    


ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
print(AMSCO(ptext,"LETTERS"))
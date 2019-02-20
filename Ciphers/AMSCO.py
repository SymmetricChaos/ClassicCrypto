# http://www.cryptogram.org/downloads/aca.info/ciphers/Amsco.pdf

from itertools import cycle
from Ciphers.UtilityFunctions import uniqueRank, groups
import random
from numpy import argsort

def AMSCO(text,key,decode=False):
    
    k = uniqueRank(key)
    print(k)

    T = list(text)
    L = []
    
    for i in cycle([1,2]):
        
        if len(T) == 0:
            break
        
        if i == 2 and len(T) > 1:
            L.append( T.pop(0) + T.pop(0) )
            
        else:
            L.append( T.pop(0) )
    
    x = groups(L,7)
    for i in x:
        print(i)
    

    


ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
AMSCO(ptext,"LETTERS")
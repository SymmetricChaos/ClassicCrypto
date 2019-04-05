from Ciphers.UtilityFunctions import validptext, validkeys, alphaToNumber, numberToAlpha
from itertools import cycle

def stretch(L,n):
    
    out = []
    for i in L:
        out += [i]*n
        
    return out
    

def recursiveKey(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    
    # Validate the inputs
    validptext(text,alphabet)
    validkeys(key,str)
    
    if len(set(alphabet)) != len(alphabet):
        raise Exception("Alphabet cannot repeat any symbols")
    
    
    
    nextkey = len(key)
    
    K = alphaToNumber(key,alphabet)
    P = [cycle(K)]
    T = alphaToNumber(text,alphabet)
    M = len(alphabet)
  
    out = []
    
    for pos,textnum in enumerate(T):
        
        if pos == nextkey:
            P.append(cycle(stretch(K,nextkey)))
            nextkey = nextkey*2
        
        s = 0
        #for i in P:
        #    n = next(i)
        #    print(n,end="")
        #    s += n
        #print()
        
        for i in P:
            s += next(i)
        
        if decode == False:
            out.append( (textnum+s) % M)
        else:
            out.append( (textnum-s) % M)
            
    return "".join(numberToAlpha(out,alphabet))
        
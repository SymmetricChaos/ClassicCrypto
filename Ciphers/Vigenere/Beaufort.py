from Ciphers.UtilityFunctions import validptext, validkeys, alphaToNumber, numberToAlpha
from itertools import cycle

# The Beaufort cipher is a sort of dual to the Vigenere cipher. The numeric
# values of the text are subtracted from the numeric values of the key. This
# provides the same degree of security sas the Vigenere but is involutive.

def beaufort(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    
    """The Beaufort cipher subtracts the text from key. This makes it a reciprocal cipher that works the same when encrypting and decrypting."""
        
    M = len(alphabet)
       
    # Validate input and convert as necessary
    validptext(text,alphabet)
    validkeys(key,str)

    # Convert both the text and key to a list of numbers
    K = cycle(alphaToNumber(key,alphabet))
    T = alphaToNumber(text,alphabet)
    
    out = []
    for keynum,textnum in zip(K,T):

        # The beaufort cipher is involutive so the decode argument is ignored
        # but still exist for compatibility.
        N = (keynum-textnum)%M
        
        out.append(N)
        
        
    return "".join(numberToAlpha(out,alphabet))

# Using multiple Beaufort ciphers has the same advantages as using multiple
# Vigenere ciphers. The key has a length equal to the least common multiple of
# the key lengths. However the cipher is not longer an involution. The keys
# must be used in reverse.
def multiBeaufort(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    
    validkeys(key,list)
    
    if decode == True:
        key.reverse()
    
    out = text
    for i in key:
        out = beaufort(out,i,alphabet=alphabet)

    return out
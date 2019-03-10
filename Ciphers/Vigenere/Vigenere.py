from Ciphers.UtilityFunctions import lcm, validptext, validkeys, alphaToNumber, numberToAlpha
from itertools import cycle

# The Vigenere cipher was the first polyalphabetic cipher invented as was once
# considered to be unbreakable as it makes simple frequency analysis of the
# ciphertext impossible. It operates as several Caesar ciphers.

def vigenere(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    
    
    # Validate the inputs
    validptext(text,alphabet)
    validkeys(key,str)
    
    if len(set(alphabet)) != len(alphabet):
        raise Exception("Alphabet cannot repeat any symbols")
    
    K = alphaToNumber(key,alphabet)
    T = alphaToNumber(text,alphabet)
    M = len(alphabet)
  
    out = []
        
    for keynum,textnum in zip(cycle(K),T):
        
        if decode == False:
            out.append( (textnum+keynum) % M)
        else:
            out.append( (textnum-keynum) % M)
        
    return "".join(numberToAlpha(out,alphabet))


# Using multiple vigenere ciphers on the same ciphertext increases security
# dramatically. If the two keys are coprime then the result is equivalent to a
# Vigenere cipher with a key equal to the product of their length but is much
# easier to remember. For example if one key has a length of 7 and the other a
# length of 10 the resulting key has a length of 70!
def multiVigenere(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    
    if type(key) != list:
        raise Exception("Must provide a list of keys")
    
    out = text
    for i in key:
        out = vigenere(out,i,decode=decode,alphabet=alphabet)
    return out

# The Trithemius cipher is not a true cipher as it has no key. However it is the
# predecessor to the Vigenere cipher. Each letter is shifted by one more than
# the previous letter.
def trithemius(text,key="",decode=False):
    
    # The key is the same every time. The key argument is kept for compatibility.
    K = [i for i in range(26)]

    # Convert the text into numbers
    N = alphaToNumber(text)

    out = []

    for keynum,textnum in zip(cycle(K),N):
        
        if decode == False:
            out.append( (textnum+keynum) % 26)
        else:
            out.append( (textnum-keynum) % 26)

    return "".join(numberToAlpha(out))
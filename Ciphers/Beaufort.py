from Ciphers.UtilityFunctions import lcm, validptext, validkeys, alphaToNumber, numberToAlpha
from itertools import cycle

# The Beaufort cipher is a sort of dual to the Vigenere cipher. The numeric
# values of the text are subtracted from the numeric values of the key. This
# provides the same degree of security sas the Vigenere but is involutive.

def beaufort(text,key,decode=False,extended=False):
    
    """
:param text: The text to be encrypyed. Must be uppercase
:param key: A keyword that is used to encrypt the text.
:param decode: Boolean. Ignored as the Beaufort cipher is reciprocal.
    """
    
    # Effect of the mode
    if extended == True:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        M = 36
    else:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        M = 26
   
    # Validate input and convert as necessary
    validptext(text,alpha)
    validkeys(key,str)

    # Convert both the text and key to a list of numbers
    K = cycle(alphaToNumber(key,alpha))
    T = alphaToNumber(text,alpha)
    
    out = []
    for keynum,textnum in zip(K,T):

        # The beaufort cipher is involutive so the decode argument is ignored
        # but still exist for compatibility.
        N = (keynum-textnum)%M
        
        out.append(N)
        
        
    return "".join(numberToAlpha(out,alpha))

# Using multiple Beaufort ciphers has the same advantages as using multiple
# Vigenere ciphers. The key has a length equal to the least common multiple of
# the key lengths. However the cipher is not longer an involution. The keys
# must be used in reverse.
def multiBeaufort(text,key,decode=False):
    
    if type(key) != list:
        raise Exception("Must provide a list of keys")
    
    if decode == True:
        key.reverse()
    
    out = text
    for i in key:
        out = beaufort(out,i)

    return out

def beaufortExample():

    print("Beaufort Example\n")
    key = "APPLES"
    print("The Key Is: {}\n".format(key))
    
    print("Normal Mode")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = beaufort(ptext,key)
    dtext = beaufort(ctext,key)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    print("\nExtended Mode")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = beaufort(ptext,key,extended=True)
    dtext = beaufort(ctext,key,extended=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
def multiBeaufortExample():

    print("Multiple Beaufort Example\n")
    key = ["ROMANCE","KINGDOMS"]
    print("The Key Is: {}\n".format(key))
    L = lcm( len(key[0]), len(key[1])  )
    print("Effective Key Length: {}\n".format(L))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = multiBeaufort(ptext,key)
    dtext = multiBeaufort(ctext,key,True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

#beaufortExample()
#multiBeaufortExample()
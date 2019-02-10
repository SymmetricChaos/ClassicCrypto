from Ciphers.UtilityFunctions import lcm

# The Beaufort cipher is a sort of dual to the Vigenere cipher. The numeric
# values of the text are subtracted from the numeric values of the key. This
# provides the same degree of security sas the Vigenere but is involutive.

def beaufort(text,key,decode=False):
    
    """
:param text: The text to be encrypyed. Must be uppercase
:param key: A keyword that is used to encrypt the text.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext
    """
    

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    T = []
    kLen = len(key)
    
    # convert the keys to lists of numbers
    K = []
    
    for i in key:
        K.append(alphabet.index(i))
    

    for ind,let in enumerate(text):
        N = alphabet.index(let)

        # The beaufort cipher is involutive so the decode argument is ignored
        # but still exist for compatibility.
        N = (K[ind%kLen]-N)%26
        
        T.append(N)
        
    for t in range(len(T)):
        T[t] = alphabet[T[t]]
        
    return "".join(T)

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
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = beaufort(ptext,key)
    dtext = beaufort(ctext,key)
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
# The autokey cipher works similarly to the Vigenere cipher but rather than
# repeated the keys over and over it extends the key by using the plaintext
# itself. In essence the plaintext is appended to the key of the Vigenere
# cipher so that it doesn't repeat in a clear pattern.


def autokey(text,key,decode=False):

    """
:param text: The text to be encrypyed. Must be alphanumeric and uppercase. The letter J will be replaced with I.
:param key: A keyword that is used to encrypt the first few letters.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext
    """
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    T = []
    
    # convert the keys to lists of numbers
    K = []
    
    for i in key:
        K.append(alphabet.index(i))
    
    if decode == False:
        for i in text:
            K.append(alphabet.index(i))

    for ind,let in enumerate(text):
        N = alphabet.index(let)

        if decode == False:
            N = (N+K[ind])%26
        else:

            N = (N-K[ind])%26
            K.append(N)

            
        T.append(N)
        
    for t in range(len(T)):
        T[t] = alphabet[T[t]]
        
    return "".join(T)

def autokeyExample():

    print("Vigenere Autokey Example\n")
    key = "APPLES"
    print("The Key Is: {}\n".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = autokey(ptext,key)
    dtext = autokey(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
# The Beaufort cipher is a sort of dual to the Vigenere cipher. The numeric
# values of the text are subtracted from the numeric values of the key. This
# provides the same degree of security sas the Vigenere but is involutive.

def beaufort(text,key,decode=False):

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

#beaufortExample()
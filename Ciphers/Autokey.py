def autokey(text,key,decode=False):

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
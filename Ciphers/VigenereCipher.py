from UtilityFunctions import modinv

def vigenere(text,key,decode=False):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    T = []
    kLen = len(key)
    
    # convert the keys to lists of numbers
    K = []
    
    for i in key:
        K.append(alphabet.index(i))
    

    for ind,let in enumerate(text):
        N = alphabet.index(let)

        if decode == False:
            N = (N+K[ind%kLen])%26
        else:
            N = (N-K[ind%kLen])%26
        
        T.append(N)
        
    for t in range(len(T)):
        T[t] = alphabet[T[t]]
        
    return "".join(T)


def multiVigenere(text,keys=["A"],decode=False):
    
    ctext = text
    for i in keys:
        ctext = vigenere(ctext,i,decode=decode)
    
    return ctext


def vigenereAutokey(text,key,decode=False):

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



def affineVigenere(text,key=[0,1],decode=False):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#"
    T = []
    kLen1 = len(key[0])
    kLen2 = len(key[1])
    
    if "#" in key[1]:
        raise Exception('cannot use # symbol in multiplicative key')
    
    # convert the keys to lists of numbers
    K1, K2, = [],[]
    for i in key[0]:
        K1.append(alphabet.find(i))
    
    for i in key[1]:
        K2.append(alphabet.find(i))

    for ind,let in enumerate(text):
        N = alphabet.index(let)

        if decode == False:
            N = (N+K1[ind%kLen1])%37
            N = (N*(K2[ind%kLen2]+1))%37
        else:
            inv = modinv(K2[ind%kLen2]+1,37)
            N = (N*inv)%37
            N = (N-K1[ind%kLen1])%37
        
        T.append(N)
    
    for t in range(len(T)):
        T[t] = alphabet[T[t]]
        
    return "".join(T)


def vigenereExample():

    print("Vigenere Example\n")
    key = "APPLES"
    print("The Key Is: {}\n".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = vigenere(ptext,key)
    dtext = vigenere(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
def vigenereAutokeyExample():

    print("Vigenere Autokey Example\n")
    key = "APPLES"
    print("The Key Is: {}\n".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = vigenereAutokey(ptext,key)
    dtext = vigenereAutokey(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    
def affineVigenereExample():

    print("Affine Vigenere Example\n")
    key = ["APPLES","TASTEGOOD"]
    print("The Key Is: {}\n".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = affineVigenere(ptext,key)
    dtext = affineVigenere(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    
#vigenereExample()
#print("\n")
#vigenereAutokeyExample()
#print("\n")
#affineVigenereExample()
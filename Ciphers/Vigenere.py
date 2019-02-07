from Ciphers.UtilityFunctions import lcm, validptext, validkeys

# The Vigenere cipher was the first polyalphabetic cipher invented as was once
# considered to be unbreakable as it makes simple frequency analysis of the
# ciphertext impossible. It operates as several Caesar ciphers.

def vigenere(text,key,decode=False):
    
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    validptext(text,alphabet)
    validkeys(key,str)

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


# Using multiple vigenere ciphers on the same ciphertext increases security
# dramatically. If the two keys are coprime then the result is equivalent to a
# Vigenere cipher with a key equal to the product of their length but is much
# easier to remember. For example if one key has a length of 7 and the other a
# length of 10 the resulting key has a length of 70!
def multiVigenere(text,key,decode=False):
    
    if type(key) != list:
        raise Exception("Must provide a list of keys")
    
    out = text
    for i in key:
        out = vigenere(out,i,decode=decode)
    return out

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
    
def multiVigenereExample():

    print("Multiple Vigenere Example\n")
    key = ["ROMANCE","KINGDOMS"]
    print("The Key Is: {}".format(key))
    L = lcm( len(key[0]), len(key[1])  )
    print("Effective Key Length: {}\n".format(L))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = multiVigenere(ptext,key)
    dtext = multiVigenere(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

#vigenereExample()
#multiVigenereExample()
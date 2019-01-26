from Ciphers.UtilityFunctions import groups
import random
from sympy import Matrix, pprint

## Hill's matrix cipher is based on the fundamental operation of linear
## algebra, matrix multiplication. This is accomplished by dividing the text
## into chunks and using modular matrix multiplication to encrypt them. 

## Although the pure form of the cipher is not very secure it was one of the
## first serious block ciphers.


# The crudest possible method of creating keys. Pick a size and randomly
# generate matrices until one of them is truly invertible.
# It can take a while to generate a key if n is more than 8.
def createMatrixKey(n):
    while True:
        L = [[random.randint(0,26) for i in range(n)] for j in range(n)]
        M = Matrix(L)
        
        # If it is signular start over
        if M.det() % 2 == 0:
            continue
        
        if M.det() % 13 == 0:
            continue
        
        return M
 
def hillCipher(text,key,decode=False):
    
    # If a list is provided turn it into a sympy Matrix
    if type(key) == list:
        key = Matrix(key)
    
    # If we are decoding invert the key
    if decode == True:
        key = key.inv_mod(26)

    # Get the dimension of the key
    N = key.shape[0]

    # Apply any nulls needed
    rem = len(text) % N
    if rem != 0:
        text += "X"*(N-rem)

    # Alphabet we are using
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    out = ""
    for i in groups(text,N):
        x = Matrix([alpha.index(let) for let in i])
        y = key.dot(x)
        out += "".join([alpha[j%26] for j in y])

    return out

def hillCipherExample():
    print("Example of the Hill Cipher\n")

    key = createMatrixKey(2)
    
    print("The key is:\n")
    pprint(key)
    print()
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = hillCipher(ptext,key)
    dtext = hillCipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

#hillCipherExample()
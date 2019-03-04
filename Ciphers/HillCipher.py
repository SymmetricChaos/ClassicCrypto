from Ciphers.UtilityFunctions import groups, factors
import random
from sympy import Matrix, pprint

## Hill's matrix cipher is based on the fundamental operation of linear
## algebra, matrix multiplication. This is accomplished by dividing the text
## into chunks and using modular matrix multiplication to encrypt them. 

## Although the pure form of the cipher is not very secure it was one of the
## first serious block ciphers.


# The crudest possible method of creating keys. Pick a size and randomly
# generate matrices until one of them is invertible modulo M.
# It can take a while to generate a key if n is more than 10.
def createMatrixKey(n,M=26):
    
    # Get the prime factors of M so we can check if it is singular
    F = factors(M,prime=True)

    
    while True:
        print("!")
        L = [[random.randint(0,M) for i in range(n)] for j in range(n)]
        mat = Matrix(L)
        
        # Check if the matrix is singular modulo M
        singular = False
        for factor in F:
            if mat.det() % factor == 0:
                singular = True
                break

        # If it is retry
        if singular == True:
            continue
        
        return mat
        

    
 
def hillCipher(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    
    M = len(alphabet)
    
    # If a list is provided turn it into a sympy Matrix
    if type(key) == list:
        key = Matrix(key)
    
    # If we are decoding invert the key
    if decode == True:
        key = key.inv_mod(M)

    # Get the dimension of the key
    N = key.shape[0]

    # Apply any nulls needed
    rem = len(text) % N
    if rem != 0:
        text += "X"*(N-rem)
    
    out = ""
    for i in groups(text,N):
        x = Matrix([alphabet.index(let) for let in i])
        y = key.dot(x)
        out += "".join([alphabet[j%M] for j in y])

    return out

def hillCipherExample():
    print("Example of the Hill Cipher\n")

    key = createMatrixKey(6)
    
    print("The key is:")
    pprint(key)
    print()
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = hillCipher(ptext,key)
    dtext = hillCipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    print("\n\nCustom Alphabet Example\n")

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#"
    key = createMatrixKey(4,len(alpha))
    
    print("The key is:")
    pprint(key)
    print("\nThe alphabet is\n{}\nWhich has length {}\n".format(alpha,len(alpha)))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = hillCipher(ptext,key,alphabet=alpha)
    dtext = hillCipher(ctext,key,decode=True,alphabet=alpha)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

#hillCipherExample()
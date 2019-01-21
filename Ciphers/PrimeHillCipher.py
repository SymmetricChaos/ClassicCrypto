from Ciphers.UtilityFunctions import groups
import random
from sympy import Matrix, pprint

# This version of the Hill Cipher operates over a finite field, significantly
# increasing the possible key space and making keys slightly easier to find.

def createMatrixKey(n):
    while True:
        L = [[random.randint(0,37) for i in range(n)] for j in range(n)]
        M = Matrix(L)
        
        # If it is singular start over
        if M.det() % 37 == 0:
            continue

        return M
            
def primeHillCipher(text,key,decode=False):
    
    # If a list is provided turn it into a sympy Matrix
    if type(key) == list:
        key = Matrix(key)
    
    # If we are decoding invert the key
    if decode == True:
        key = key.inv_mod(37)

    # Get the dimension of the key
    N = key.shape[0]

    # Apply nulls at the end if needed.
    rem = len(text) % N
    if rem != 0:
        text += "X"*(N-rem)


    # The alphabet we are using
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#"

    out = ""
    for i in groups(text,N):
        x = Matrix([alpha.index(let) for let in i])
        y = key.dot(x)
        out += "".join([alpha[j%37] for j in y])

    return out

def primeHillCipherExample():
    print("Example of the Prime Hill Cipher\n")

    key = createMatrixKey(6)
    
    
    print("The key is:\n")
    pprint(key)
    print()
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = primeHillCipher(ptext,key)
    dtext = primeHillCipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#primeHillCipherExample()
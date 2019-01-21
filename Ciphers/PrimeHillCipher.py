from Ciphers.UtilityFunctions import groups
import random
from sympy import Matrix, pprint

# This version of the Hill Cipher operates over a finite field, significantly
# increasing the possible key space and making keys slightly easier to find.

def createMatrixKey(n):
    while True:
        L = [[random.randint(0,37) for i in range(n)] for j in range(n)]
        M = Matrix(L)
        A = M * M.inv_mod(37)
        f = lambda x: x % 37
        A = A.applyfunc(f)
        
        if A == Matrix.eye(n):
            return M
            
def primeHillCipher(text,key,decode=False):
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#"
    
    if decode == True:
        key = key.inv_mod(37)

    N = key.shape[0]

    # Apply nulls at the end if needed.
    b,rem = divmod(len(text),N)
    if rem != 0:
        text += "X"*(N-rem)

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
    
primeHillCipherExample()
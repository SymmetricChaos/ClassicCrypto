from Ciphers.UtilityFunctions import modinv,egcd
import numpy as np
from numpy.linalg import det,inv

## Hill's matrix cipher is based on the fundamental operation of linear
## algebra, matrix multiplication. This is accomplished by dividing the text
## into chunks and using modular matrix multiplication to encrypt them. 

## Although the pure form of the cipher is not very secure it was one of the
## first serious block ciphers.

def modmatinv(M,n):
    d = int(det(M))
    i = modinv(d%n,n)
    
    invM = inv(M)*d*i
    invM = np.matrix.round(invM)
    invM = invM.astype(int)%n
    
    return invM

# The crudest possible method of creating keys. Pick a size and randomly
# generate matrices until one of them is truly invertible.
# It can take a while to generate a key if n is more than about 9.
def createMatrixKey(n):
    while True:
        M = np.matrix(np.random.randint(26, size=(n, n)))
        d = int(det(M))
        g,x,y = egcd(d%26,26)
        if g == 1:
            if np.all( M.dot(modmatinv(M,26))%26 == np.identity(n) ):
                return M
 
def hillCipher(text,key,decode=False):
    if decode == True:
        key = modmatinv(key,26)

    N = key.shape[0]

    b,rem = divmod(len(text),N)
    if rem != 0:
        text += "X"*(N-rem)

    out = ""
    for i in range(len(text)//N):
        x = [ord(j)-65 for j in text[i*N:N+i*N]]
        y = (x*key%26)+65
        out += "".join([chr(j) for j in y.flat])

    return out

def hillCipherExample():
    print("Example of the Hill Cipher\n")

    key = createMatrixKey(7)
    
    print("The key is \n{}\n".format(key))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = hillCipher(ptext,key)
    dtext = hillCipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
## Hill's matrix cipher is based on the fundamental operation of linear
## algebra, matrix multiplication. This is accomplished by dividing the text
## into chunks and using modular matrix multiplication to encrypt them. 

## Although the pure form of the cipher is not very secure it was one of the
## first serious block ciphers.

import numpy as np
from UtilityFunctions import modinv
from numpy.linalg import det,inv


def modmatinv(M,n):
    d = int(det(M))
    i = modinv(d%n,n)
    
    invM = inv(M)*d*i
    invM = np.matrix.round(invM)
    invM = invM.astype(int)%n
    
    return(invM)

def hillcipher(text,key,decode=False):
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
    key = np.matrix([[12,14,24,4,6,4,13],
                [23,24,4,17,24,10,15],
                [17,0,18,6,22,22,11],
                [1,15,11,9,10,13,1],
                [9,9,16,9,18,24,6],
                [1,9,17,15,14,4,19],
                [24,20,5,0,15,21,12]])
    print("The key is \n{}\n".format(key))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = hillcipher(ptext,key)
    dtext = hillcipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

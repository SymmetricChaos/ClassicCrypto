## Hill's matrix cipher is based on the fundamental operation of linear
## algebra, matrix multiplication. This is accomplished by dividing the text
## into chunks and using modular matrix multiplication to encrypt them. 

## Although the pure form of the cipher is not very secure it was one of the
## first serious block ciphers.

import numpy as np
from numpy.linalg import det,inv

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def modmatinv(M,n):
    d = int(det(M))
    i = modinv(d%n,n)
    
    invM = inv(M)*d*i
    invM = np.matrix.round(invM)
    invM = invM.astype(int)%n
    
    return(invM)

def hillcipher(s,k,decode=False):
    if decode == True:
        k = modmatinv(k,26)
        
    N = k.shape[0]
    
    b,rem = divmod(len(s),N)
    if rem != 0:
        s += "X"*(N-rem)

    out = ""
    for i in range(len(s)//N):
        x = [ord(j)-65 for j in s[i*N:N+i*N]]
        y = (x*k%26)+65
        out += "".join([chr(j) for j in y.flat])
    
    return out


key = np.matrix([[12,14,24,4,6,4,13],
                [23,24,4,17,24,10,15],
                [17,0,18,6,22,22,11],
                [1,15,11,9,10,13,1],
                [9,9,16,9,18,24,6],
                [1,9,17,15,14,4,19],
                [24,20,5,0,15,21,12]])


plaintext = "THISFORMOFMATRIXCIPHERWASDEVELOPEDBYLESTERHILLITWASONEOFTHEFIRSTCIPHERSTOALLOWENCRYPTIONTHATOPERATEDONALARGENUMBEROFSYMBOLSATONCEXXXX"

ctext = hillcipher(plaintext,key)
print(ctext)
decoded = hillcipher(ctext,key,decode=True)
print("Decode Matches Plaintext:",decoded == plaintext)
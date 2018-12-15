from ModularArithmetic import *

def caesar(s,k,decode=False):
    s = s.upper()
    if decode == True:
        k = 26-k
    return "".join([chr((ord(i)-65+k)%26+65) for i in s])

def affine(s,k=[0,1],decode=False):
    
    # In this basic form of affine cipher the multiplication cannot be a
    # multiple of 2 or 13 since they have no inverse modulo 26.
    if k[1] % 2 == 0:
        raise Exception('multiplicative part has no inverse')
    if k[1] % 13 == 0:
        raise Exception('multiplicative part has no inverse')
    
    T = []
    
    for i in s:
        N = ord(i)-65
        
        if decode == False:
            N = (N+k[0])%26
            N = (N*k[1])%26
        else:
            inv = modinv(k[1],26)
            N = (N*inv)%26
            N = (N-k[0])%26
        
        T.append(chr(N+65))
        
    return "".join(T)

def substitution(s,k,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    
    # Derive the internally used key from the input
    # We use only the unique letters of the key and then
    # follow them with the remaining letters of the alphabet
    key = ""
    for letter in k:
        if letter not in key:
            key += letter
    for letter in alpha:
        if letter not in key:
            key += letter
            
    if decode == False:
        for i in s:
            out.append(key[alpha.index(i)])
    if decode == True:
        for i in s:
            out.append(alpha[key.index(i)])
    
    return "".join(out)



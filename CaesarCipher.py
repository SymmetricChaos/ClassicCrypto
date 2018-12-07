def caesar(s,k,decode=False):
    s = s.upper()
    if decode == True:
        k = 26-k
    return "".join([chr((ord(i)-65+k)%26+65) for i in s])

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

def affine(s,k1,k2,decode=False):
    
    if k2 % 2 == 0:
        raise Exception('multiplicative part has no inverse')
    if k2 % 13 == 0:
        raise Exception('multiplicative part has no inverse')
    
    T = []
    
    for i in s:
        N = ord(i)-65
        
        if decode == False:
            N = (N+k1)%26
            N = (N*k2)%26
        else:
            inv = modinv(k2,26)
            N = (N*inv)%26
            N = (N-k1)%26
        
        T.append(chr(N+65))
        
    return "".join(T)
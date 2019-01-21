from Ciphers.UtilityFunctions import modinv

# The affine cipher is very similar but requires more of an understanding of
# modular arithmetic. Each letter is assigned a number with A = 0, B = 1, and
# so on. Then each number has a value added to it and it multiplied by a value.
# The result is reduced modulo 26. Then the numbers are turned back into
# letters using the same rules 0 = A, 1 = B, 2 = C.

def affine(text,key=[0,1],decode=False):
    
    # In this basic form of affine cipher the multiplication cannot be a
    # multiple of 2 or 13 since they have no inverse modulo 26.
    if key[1] % 2 == 0:
        raise Exception('multiplicative part has no inverse')
    if key[1] % 13 == 0:
        raise Exception('multiplicative part has no inverse')
    
    T = []
    
    for i in text:
        N = ord(i)-65
        
        if decode == False:
            N = (N+key[0])%26
            N = (N*key[1])%26
        else:
            inv = modinv(key[1],26)
            N = (N*inv)%26
            N = (N-key[0])%26
        
        T.append(chr(N+65))
        
    return "".join(T)

def affineExample():
    print("Example of the Affine Cipher\n")
    
    key = [3,7]

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = affine(ptext,key)
    dtext = affine(ctext,key,decode=True)
    print("\nPlaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
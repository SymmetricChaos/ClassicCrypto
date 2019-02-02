from Ciphers.UtilityFunctions import modinv

# The affine cipher is very similar but requires more of an understanding of
# modular arithmetic. Each letter is assigned a number with A = 0, B = 1, and
# so on. Then each number is multiplied by a certain value followed by addition
# by addition by some number.

def affine(text,key=[0,1],decode=False):
    
    """
:param text: The text to be encrypyed. Must be alphanumeric and uppercase. The letter J will be replaced with I.
:param key: A list of two integers. The first is used for multiplication. The second for addition.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext
    """
    
    # In this basic form of affine cipher the multiplication cannot be a
    # multiple of 2 or 13 since they have no inverse modulo 26.
    if key[0] % 2 == 0:
        raise Exception('multiplicative part has no inverse')
    if key[0] % 13 == 0:
        raise Exception('multiplicative part has no inverse')
    
    T = []
    
    for i in text:
        N = ord(i)-65
        
        if decode == False:
            N = (N*key[0])%26
            N = (N+key[1])%26
        else:
            inv = modinv(key[0],26)
            N = (N-key[1])%26
            N = (N*inv)%26
        
        T.append(chr(N+65))
        
    return "".join(T)


def affineExample():
    print("Example of the Affine Cipher\n")
    
    key = [3,7]
    print("The Key is: Mult {} then Add {}".format(key[0],key[1]))

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = affine(ptext,key)
    dtext = affine(ctext,key,decode=True)
    print("\nPlaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

#affineExample()
from Ciphers.UtilityFunctions import modinv, factors, alphaToNumber, numberToAlpha, validptext, validkeys

# The affine cipher is very similar but requires more of an understanding of
# modular arithmetic. Each letter is assigned a number with A = 0, B = 1, and
# so on. Then each number is multiplied by a certain value followed by addition
# by addition by some number.

def affine(text,key=[0,1],decode=False,alphabet=""):
    
    """
:param text: The text to be encrypyed. Must be alphanumeric and uppercase. The letter J will be replaced with I.
:param key: A list of two integers. The first is used for multiplication. The second for addition.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext
    """
    
    if alphabet == "":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #
    validptext(text,alphabet)
    validkeys(key,[int,int])
    
    # The length of the alphabet and its factors
    M = len(alphabet)
    F = factors(M)
    
    # A common error for an affine cipher is using a multiplicative constant
    # that has no inverse modulo the length of the alphabet. That constant must
    # be coprime to the factors of the modulus.
    # For the usual 26 letter alphabet this means 13 and all even numbers are
    # forbidden.
    for fac in F:
        if key[0] % fac == 0:
            raise Exception('multiplicative part has no inverse')
    
    # Convert the text to numbers
    T = alphaToNumber(text,alphabet)
    
    # Get the inverse of the multiplicative constant
    inv = modinv(key[0],M)
    
    out = []
    
    for textnum in T:
        
        if decode == False:
            out.append( (textnum * key[0] + key[1]) % M )
        else:
            out.append( ((textnum - key[1]) * inv) % M )
        
        
    return "".join(numberToAlpha(out,alphabet))


def affineExample():
    print("Example of the Affine Cipher\n")
    
    key = [7,11]
    print("The Key is: Multiply by {} then Add {}".format(key[0],key[1]))

    print("\nIn Normal Mode")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = affine(ptext,key)
    dtext = affine(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    print("\n\nUsing Custom Alphabet:\n{}".format(alpha))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = affine(ptext,key,alphabet=alpha)
    dtext = affine(ctext,key,decode=True,alphabet=alpha)
    print("\nPlaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

#affineExample()
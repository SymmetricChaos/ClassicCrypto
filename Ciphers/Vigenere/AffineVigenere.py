from Ciphers.UtilityFunctions import modinv, alphaToNumber, numberToAlpha
from itertools import cycle


def affineVigenere(text,key=["A","A"],decode=False):
    
    """
:param text: The text to be encrypyed. Must be alphanumeric and uppercase. The letter J will be replaced with I.
:param key: A list of two integers. The first is used for mutiplication. The second for addition.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext
    """
    
    # Error if an invalid key value is used
    if "#" in key[0]:
        raise Exception('cannot use # symbol in multiplicative key')
    
    # The 37 symbol alphabet being used
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#"
    
    # Convert the plaintext and keys to lists of numbers
    T = alphaToNumber(text,alphabet)
    K1, K2, = alphaToNumber(key[0],alphabet),alphaToNumber(key[0],alphabet)
    

    out = []
    # Cycle through the two keys as much as needed as we go through the key
    for keynum1,keynum2,textnum in zip(cycle(K1),cycle(K2),T):

        N = textnum
        
        # When encoding multiply and then add
        # When decoding multiply by the inverse then subtract
        if decode == False:
            N = (N*(keynum1 + 1))%37
            N = (N+keynum2) % 37
        else:
            inv = modinv(keynum1 + 1,37)
            N = (N-keynum2)%37
            N = (N*inv)%37
        
        out.append(N)
    
    
    return "".join(numberToAlpha(out,alphabet))

def affineVigenereExample():

    print("Affine Vigenere Example\n")
    key = ["APPLES","TASTEGOOD"]
    print("The Key Is: {}\n".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = affineVigenere(ptext,key)
    dtext = affineVigenere(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#affineVigenereExample()
from Ciphers.UtilityFunctions import validptext, validkeys, alphaToNumber, numberToAlpha

# The autokey cipher works similarly to the Vigenere cipher but rather than
# repeated the keys over and over it extends the key by using the plaintext
# itself. In essence the plaintext is appended to the key of the Vigenere
# cipher so that it doesn't repeat in a clear pattern.


def autokey(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ",mode="vigenere"):

    """
:param text: The text to be encrypyed or decrypted. Must be uppercase.
:param key: A keyword that is used to encrypt the first few letters.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext.
:param mode: String to select between vigenere and beaufort modes.
    """
    
    M = len(alphabet)
    
    validptext(text,alphabet)
    validkeys(key,str)
    
    if mode in ["v","vig","vigenere"]:
        mode = "vigenere"
    elif mode in ["b","beau","beaufort"]:
        mode = "beaufort"
    else:
        raise Exception("{} is not a valid mode".format(mode))
    
    # Convert the text to numbers
    T = alphaToNumber(text,alphabet)
    # Conver the key to numbers
    K = alphaToNumber(key,alphabet) 
    
    # When encoding append the text to the key, we use a different method when
    # decoding
    if decode == False:
        K += T

    out = []
    if mode == "vigenere":
        for keynum,textnum in zip(K,T):
            if decode == False:
                out.append( (textnum+keynum) % M )
            else:
                # Decode a letter then add it to the keystrean
                out.append( (textnum-keynum) % M )
                K.append( out[-1] )
        
    if mode == "beaufort":
        for keynum,textnum in zip(K,T):
            if decode == False:
                out.append( (keynum-textnum) % M )
            else:
                # Decode a letter then add it to the keystrean
                out.append( (keynum-textnum) % M )
                K.append( out[-1] )
                

    return "".join(numberToAlpha(out,alphabet))

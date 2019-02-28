from Ciphers.UtilityFunctions import validptext, validkeys, alphaToNumber, numberToAlpha

# The autokey cipher works similarly to the Vigenere cipher but rather than
# repeated the keys over and over it extends the key by using the plaintext
# itself. In essence the plaintext is appended to the key of the Vigenere
# cipher so that it doesn't repeat in a clear pattern.


def autokey(text,key,decode=False,mode="vigenere"):

    """
:param text: The text to be encrypyed. Must be uppercase.
:param key: A keyword that is used to encrypt the first few letters.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext.
:param mode: String to select between vigenere and beaufort modes.
    """
    
    validptext(text,"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    validkeys(key,str)
    
    if mode in ["v","vig","vigenere"]:
        mode = "vigenere"
    elif mode in ["b","beau","beaufort"]:
        mode = "beaufort"
    else:
        raise Exception("{} is not a valid mode".format(mode))
    
    # Convert the text to numbers
    T = alphaToNumber(text)
    # Conver the key to numbers
    K = alphaToNumber(key) 
    
    # When encoding append the text to the key, we use a different method when
    # decoding
    if decode == False:
        K += T

    out = []
    for keynum,textnum in zip(K,T):

        if mode == "vigenere":
            if decode == False:
                out.append( (textnum+keynum)%26 )
            else:
                # Decode a letter then add it to the keystrean
                out.append( (textnum-keynum)%26 )
                K.append( out[-1] )
        
        if mode == "beaufort":
            if decode == False:
                out.append( (keynum-textnum)%26 )
            else:
                # Decode a letter then add it to the keystrean
                out.append( (keynum-textnum)%26 )
                K.append( out[-1] )       
                

    return "".join(numberToAlpha(out))

def autokeyExample():

    print("Autokey Example\n")
    key = "APPLES"
    print("The Key Is: {}\n".format(key))
    
    for mode in ["vigenere","beaufort"]:
        print("\nIn {} mode".format(mode))
        ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
        ctext = autokey(ptext,key,mode=mode)
        dtext = autokey(ctext,key,decode=True,mode=mode)
        print("Plaintext is:  {}".format(ptext))
        print("Ciphertext is: {}".format(ctext))
        print("Decodes As:    {}".format(dtext))
    
autokeyExample()
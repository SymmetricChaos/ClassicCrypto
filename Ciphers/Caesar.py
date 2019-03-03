from Ciphers.UtilityFunctions import validptext, validkeys, alphaToNumber, numberToAlpha

# The caesar cipher, named after Julius Caesar who is said to have used it to
# protect his military secrets. Every letter is shifted a certain number of
# positions along the alphaet. So for a caesar cipher with a key of 3 the
# the letter A becomes D, while M becomes P, and X becomes A. To decode the
# cipher the letters are shifted back. The popular ROT13 is simply the caesar
# cipher with a key of 13.

def caesar(text,key,decode=False,alphabet=""):

    if alphabet == "":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if len(set(alphabet)) != len(alphabet):
        raise Exception("Alphabet cannot repeat any symbols")
    
    
    M = len(alphabet)
    T = alphaToNumber(text,alphabet)
    
    # Allow key to be specified by letter
    if type(key) == str:
        if key in alphabet:
            key = alphabet.index(key)
    

    validptext(text,alphabet)
    validkeys(key,int)
    
    if decode == True:
        key = M-key
        
    out = []
    for i in T:
        # Shift the number by the key value
        out.append( (i + key) % M )
    
    return "".join(numberToAlpha(out,alphabet))



# A very popular version of the caesar cipher is the ROT13 version. The shift
# is always 13 so there is no key and it is not a true cipher. However it is 
# interesting as an example of involutive function, applying it twice gets the
# original input.
# Both the key and decode arguments are ignored but are included for 
# compatibility with other functions.
def ROT13(text,key=None,decode=False):
    return caesar(text,13)

def caesarExample():
    print("Caesar Cipher Example\n")
    key = 17
    print("The Key Is: {}\n".format(key))
    
    print("\nStandard Mode")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = caesar(ptext,key)
    dtext = caesar(ctext,key,decode=True)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    print("Decodes As:\n{}".format(dtext))
    
    print("\nExtended Mode")
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    ptext = "TheQuickBrownFoxJumpsOverTheLazyDog"
    ctext = caesar(ptext,key,alphabet=alpha)
    dtext = caesar(ctext,key,decode=True,alphabet=alpha)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    print("Decodes As:\n{}".format(dtext))
    
def ROT13Example():
    print("ROT13 Example\n")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = ROT13(ptext)
    dtext = ROT13(ctext)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    print("Decodes As:\n{}".format(dtext))

#caesarExample()
#ROT13Example()
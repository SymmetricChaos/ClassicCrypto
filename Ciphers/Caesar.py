from Ciphers.UtilityFunctions import validptext, validkeys

# The caesar cipher, named after Julius Caesar who is said to have used it to
# protect his military secrets. Every letter is shifted a certain number of
# positions along the alphaet. So for a caesar cipher with a key of 3 the
# the letter A becomes D, while M becomes P, and X becomes A. To decode the
# cipher the letters are shifted back. The popular ROT13 is simply the caesar
# cipher with a key of 13.

def caesar(text,key,decode=False,extended=False):
    text = text.upper()
    
    if extended == True:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        M = 36
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        M = 26
    
    # Allow key to be specified by letter
    if type(key) == str:
        if key in alphabet:
            key = alphabet.index(key)
    

    validptext(text,alphabet)
    validkeys(key,int)
    
    if decode == True:
        key = M-key
        
    out = []
    for i in text:
        # Convert each letter to its numeric values
        val = alphabet.index(i)
        # Shift the number by the key value
        val = (val + key) % M
        # Convert back to a letter
        out.append(alphabet[val])
    return "".join(out)

# Yes we could do this in one line as
# return "".join([chr((ord(i)-65+key)%26+65) for i in text])
# But these ciphers are meant to be easy to read and interpret so we just make
# explicit reference to the alphabet used.

def caesarCustom(text,key,alphabet="",decode=False):

    if alphabet == "":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Allow key to be specified by letter
    if type(key) == str:
        if key in alphabet:
            key = alphabet.index(key)
    

    validptext(text,alphabet)
    validkeys(key,int)
    
    if decode == True:
        key = len(alphabet)-key
        
    out = []
    for i in text:
        # Convert each letter to its numeric values
        val = alphabet.index(i)
        # Shift the number by the key value
        val = (val + key) % len(alphabet)
        # Convert back to a letter
        out.append(alphabet[val])
    return "".join(out)


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
    key = 3
    print("The Key Is: {}\n".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = caesar(ptext,key)
    dtext = caesar(ctext,key,decode=True)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    print("Decodes As:\n{}".format(dtext))
    
def caesarCustomExample():
    print("Caesar Cipher Example\n")
    key = 41
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"
    print("The Key Is: {}\n".format(key))
    print("Custom Alphabet:\n{}".format(alphabet))
    
    ptext = "TheQuickBrownFoxJumpsOverTheLazyDog"
    ctext = caesarCustom(ptext,key,alphabet=alphabet)
    dtext = caesarCustom(ctext,key,decode=True,alphabet=alphabet)
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
#caesarCustomExample()
#ROT13Example()
# The caesar cipher, named after Julius Caesar who is said to have used it to
# protect his military secrets. Every letter is shifted a certain number of
# positions along the alphaet. So for a caesar cipher with a key of 3 the
# the letter A becomes D, while M becomes P, and X becomes A. To decode the
# cipher the letters are shifted back. The popular ROT13 is simply the caesar
# cipher with a key of 13.

def caesar(text,key,decode=False):
    text = text.upper()
    
    if decode == True:
        key = 26-key
        
    out = []
    for i in text:
        # Convert each letter to a numeric value the 65 is there because the
        # ASCII values for capital letters start there
        val = ord(i)-65
        # Shift the number by the key value
        val = (val + key) %26
        # Convert back to a letter
        out.append(chr(val+65))
    return "".join(out)

# Yes we could do this in one line as
# return "".join([chr((ord(i)-65+key)%26+65) for i in text])
# But these ciphers are meant to be easy to read,


def caesarExample():
    print("Caesar Cipher Example\n")
    key = 1
    print("The Key Is: {}\n".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = caesar(ptext,key)
    dtext = caesar(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#caesarExample()
# A bunch of functions we need for various reasons kept here for neatness.

# Many ciphers need to create a permutation of the alphabet. A common way to do
# this for classical cryptography is to specify a key. The letters of the key
# are form the beginning of the new alphabet, skipping any repetition, and then
# the remaining letters of the alphabet are placed in order after them.

# For example the keyword CRYPTOGRAM produces
# CRYPTOGAMBDEFHIJKLNQSUVWXZ

def alphabetPermutation(key,alphabet=""):
    if alphabet == "":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for letter in key:
        if letter not in alphabet:
            raise Exception('key does not fit with alphabet')
    
    k = ""
    for letter in key:
        if letter not in k:
            k += letter
    for letter in alphabet:
        if letter not in k:
            k += letter
    
    return k

# A very simple function for testing if inputs matches output
def decodetest(text,keys,fun):
    ctext = fun(text,keys)
    dtext = fun(ctext,keys,decode=True)
    if text == dtext[:len(text)]:
        print("Success")
    else:
        raise Exception("Decode Error With {}".format(fun.__name__))



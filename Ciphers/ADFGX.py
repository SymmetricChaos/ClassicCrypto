from itertools import product
from Ciphers.UtilityFunctions import alphabetPermutation, groups
from Ciphers.ColumnarTransport import columnarTransport

# The ADFGX cipher is an important early example of a fractionated cipher that
# produces Shannon's "confusion" in the ciphertext. That is the symbols of the
# ciphertext depend on many parts of the plaintext.
        
# A modified polybius square is used. Historically it used ADFGX rather than 
# 12345, hence the name.


def ADFGX(text,keys=["A",[0,1]],decode=False):
    
    while len(text) % len(keys[1]) != 0:
        text += "X"
        
    
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alpha = alphabetPermutation(keys[0],alpha)
    # Replace 
    text = text.replace("J","I")
    
    pairs = product("ADFGX",repeat=2)
    
    D1 = {}
    D2 = {}
    for letter,pair in zip(alpha,pairs):
        D1[letter] = "".join(pair)
        D2["".join(pair)] = letter

    # The ADFGX cipher has a roughly symmetric encode and decoding process
    # the only difference is that the columnar transport is reversed.

    # Turn every letter into a pair of symbols
    ctext = "".join([D1[i] for i in text])
    # Scramble the symbols, this will break apart some of the pairs
    ctext = columnarTransport(ctext,keys[1],decode=decode)
    # Now take the scrambled symbols and turn them back into letters
    ctext = groups(ctext,2)
    ctext = "".join([D2[i] for i in ctext])

    return ctext

def ADFGXExample():
    
    print("Example of the ADFGX Cipher")
    
    key = ["ZEBRAS","TABLE"]
    
    print("They Keys Are:\n{}\n{}".format(key[0],key[1]))

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = ADFGX(ptext,key)
    dtext = ADFGX(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#ADFGXExample()
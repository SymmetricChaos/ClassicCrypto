from itertools import product
from Ciphers.UtilityFunctions import alphabetPermutation, groups
from Ciphers.ColumnarTransport import columnarTransport

# A version of the ADFGX that allows the use of numbers

def ADFGVX(text,keys=["A",[0,1]],decode=False):
    
    while len(text) % len(keys[1]) != 0:
        text += "X"
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    alpha = alphabetPermutation(keys[0],alpha)
    
    pairs = product("ADFGVX",repeat=2)
    
    D1 = {}
    D2 = {}
    for letter,pair in zip(alpha,pairs):
        D1[letter] = "".join(pair)
        D2["".join(pair)] = letter

    # Turn every letter into a pair of symbols
    ctext = "".join([D1[i] for i in text])
    # Scramble the symbols, this will break apart some of the pairs
    ctext = columnarTransport(ctext,keys[1],decode=decode)
    # Now take the scrambled symbols and turn them back into letters
    ctext = groups(ctext,2)
    ctext = "".join([D2[i] for i in ctext])

    return ctext

def ADFGVXExample():
    
    print("Example of the ADFGX Cipher")
    
    key = ["715ZEBRAS290","TABLES"]
    
    print("They Keys Are:\n{}\n{}".format(key[0],key[1]))

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = ADFGVX(ptext,key)
    dtext = ADFGVX(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#ADFGVXExample()
from itertools import product
from UtilityFunctions import alphabetPermutation, groups
from ColumnarTransport import columnarTransport


# The ADFGX cipher is an important early example of a fractionated cipher that
# produces Shannon's "confusion" in the ciphertext. That is the symbols of the
# ciphertext depend on many parts of the plaintext.

# A significantly more secure cipher is the ADFGVX variant which extends the
# alphabet to also contain symbols. This allows shorter messages that give the
# attacker less to work with.

def ADFGX(text,keys=["A",[0,1]],decode=False):
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

def ADFGVX(text,keys=["A",[0,1]],decode=False):
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
    
def ADFGXexample():

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = ADFGX(ptext,["ZEBRAS",[1,4,2,5,0,3]])
    dtext = ADFGX(ctext,["ZEBRAS",[1,4,2,5,0,3]],decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    

def ADFGVXexample():

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = ADFGVX(ptext,["17ZEBRAS529",[1,4,2,5,0,3]])
    dtext = ADFGVX(ctext,["17ZEBRAS529",[1,4,2,5,0,3]],decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))




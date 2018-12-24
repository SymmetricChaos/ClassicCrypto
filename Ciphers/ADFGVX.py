from itertools import product
import sys
#sys.path.insert(0, 'C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto')
from UtilityFunctions import alphabetPermutation, groups
sys.path.insert(0, 'C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SubstitutionCiphers\\')
from ColumnarTransport import columnarTransport


# The ADFGX cipher is an important early example of a fractionated cipher

def ADFGVX(text,keys=["A",[0,1]],decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    alpha = alphabetPermutation(keys[0],alpha)
    
    pairs = product("ADFGVX",repeat=2)
    
    D1 = {}
    D2 = {}
    for letter,pair in zip(alpha,pairs):
        D1[letter] = "".join(pair)
        D2["".join(pair)] = letter

    # The ADFGVX cipher has a roughly symmetric encode and decoding process
    # the only difference is that the columnar transport is reversed.

    # Turn every letter into a pair of symbols
    ctext = "".join([D1[i] for i in text])
    # Scramble the symbols, this will break apart some of the pairs
    ctext = columnarTransport(ctext,keys[1],decode=decode)
    # Now take the scrambled symbols and turn them back into letters
    ctext = groups(ctext,2)
    ctext = "".join([D2[i] for i in ctext])

    return ctext
    


ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
ctext = ADFGVX(ptext,["17ZEBRAS529",[1,4,2,5,0,3]])
dtext = ADFGVX(ctext,["17ZEBRAS529",[1,4,2,5,0,3]],decode=True)
print(ptext)
print(ctext)
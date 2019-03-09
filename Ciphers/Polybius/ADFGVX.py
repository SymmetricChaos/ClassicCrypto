from itertools import product
from Ciphers.UtilityFunctions import alphabetPermutation, groups, makeSquare
from Ciphers.Transposition.ColumnarTransport import columnarTransport

# A version of the ADFGX that allows the use of numbers. The polybius square is
# 6x6 instead of 5x5

def ADFGVX(text,keys=["A",[0,1]],decode=False,printkey=False):
    
    """
:param text: The text to be encrypyed. Must be alphanumeric and uppercase.
:param keys: Two keywords, the first to prepare a 6x6 square a the second to control a columnar transport cipher.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext
    """

    
    while len(text) % len(keys[1]) != 0:
        text += "X"
    
    alpha = alphabetPermutation(keys[0],"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    
    sq = makeSquare(keys[0],mode="EX")
    
    if printkey == True:
        for i in range(6):
            print(" ".join(sq[i]))

    
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

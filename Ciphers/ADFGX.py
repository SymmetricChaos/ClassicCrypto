from itertools import product
from Ciphers.UtilityFunctions import alphabetPermutation, groups, makeSquare
from Ciphers.ColumnarTransport import columnarTransport

# The ADFGX cipher is an important early example of a fractionated cipher that
# successfully causes each character of the ciphertext to depend on characters 
# from distant parts of the plaintext.

# This is accomplished by first using a polybius square to divide the plaintext
# into pairs of symbols (historically it used ADFGX rather than 12345) and then
# it uses columnar transport to shuffle the symbols. Finally the symbols are
# converted back to letters.



def ADFGX(text,keys=["A",[0,1]],decode=False,printkey=False):
    
    """
:param text: The text to be encrypyed. Must be alphanumeric and uppercase. The letter J will be replaced with I.
:param keys: Two keywords, the first to prepare a 5x5 square a the second to control a columnar transport cipher.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext
    """
    
    # Adjust the text if necessary
    text = text.replace("J","I")
    while len(text) % len(keys[1]) != 0:
        text += "X"
        
    
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alpha = alphabetPermutation(keys[0],alpha)

    
    if printkey == True:
        sq = makeSquare(keys[0],mode="EX")
        for i in range(6):
            print(" ".join(sq[i]))
    
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
    
    print("Example of the ADFGX Cipher\n")
    
    key = ["ZEBRAS","TABLES"]
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    
    print("They Polybius Square:")
    ADFGX(ptext,key,printkey=True)
    print("\nThe Columnar Transport Key:")
    print(key[1],end="\n\n")

    ctext = ADFGX(ptext,key)
    dtext = ADFGX(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    print("\nNotice that the J in the word JUMP has become I.")
    
#ADFGXExample()
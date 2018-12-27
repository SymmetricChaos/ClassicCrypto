# The DRYAD cipher was used by the US Army as a method for quickly encoding
# numeric information. A page of DRYAD consists of twenty six scrambled
# alphabets. For this implementation the Mersenne Twister is used to convert a
# number into such a page. Cryptographic weaknesses in the Mersenne Twister
# algorithm can likely be exploited. For truly secure DRYAD pages a stronger
# source of randomess is needed.

# There are several valid ways to use the DRYAD page for encryption. This 
# variation uses six letter chunks. Each chunk is a letter indicating the row
# followed by five encrypted letters. The row to use in each chunk is chosen
# randomly. To allow the encryption of long messages rows may be reused, though
# this significantly weakens the cipher.

import random
from UtilityFunctions import groups

def DRYAD(text,key,decode=False,codepage=False):
    
    # Use the key value to generate a random DRYAD page
    page = []
    random.seed(key)
    for i in range(26):
        L = [let for let in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        random.shuffle(L)
        pos = 0
        row = []
        for chunk in [4,3,3,2,2,3,2,2,2,2]:
            row.append("".join(L[pos:pos+chunk]))
            pos += chunk
        page.append(row)

    # If one wants to simply produce a DRYAD codepage this does so
    if codepage == True:
        ctr = 0
        for let,row in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",page):
            if ctr % 4 == 0:
                print("\n       0   1   2  3  4   5  6  7  8  9")
            ctr += 1
            print(let,":"," ".join(row))
            
    # Now reset the random seed
    random.seed()
    
    if decode == False:
        out = []
        for grp in groups(text,5):
            row = random.choice([n for n in range(26)])
            # write down the letter indicating the row we are using
            out.append( chr(row+65) )
            # Pick a random letter from the options to represent that digit
            for digit in grp:
                out.append( random.choice(page[row][int(digit)]) )
            out.append(" ")
        # The [:-1] removes the trailing space
        return "".join(out)[:-1]
            
    if decode == True:
        out = []
        text = text.split(" ")
        for section in text:
            code = page[ord(section[0])-65]
            for letter in section[1:]:
                for x,y in enumerate(code):
                    if letter in y:
                        out.append(str(x))
        return "".join(out)

page = random.getrandbits(64)
ptext = "213165587194201"
ctext = DRYAD(ptext,page)
dtext = DRYAD(ctext,page,decode=True)

print(ptext)
print(ctext)
print(dtext)
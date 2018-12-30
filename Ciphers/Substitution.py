from UtilityFunctions import alphabetPermutation, groups, modinv,egcd
import random
import numpy as np
from numpy.linalg import det,inv




# The straddling checkerboard is a form of substitution cipher that converts
# each letter into a variable length commaless code in a way best understood
# by example. Like the polybius square the alphabet is placed into a grid and
# the letters are encoded as the corresponding row and column.

#    0 1 2 3 4 5 6 7 8 9
#  | A B C D   E F   G H
# 4| I J K L M N O P Q R
# 7| S T U V W X Y Z

# So in this example the phrase FLEEATONCE becomes
# 6 43 5 5 0 71 46 45 2 5
# Which can be read without spaces as
# 64355071464525
# There is no ambiguity because every two digit code MUST start with a 4 or a 7
# while NO single digit code can ever start with 4 or 7.

def straddlingCheckerboard(text,keys=["A",[0,1]],decode=False):

    if len(keys) != 2:
        raise Exception('must provide both keys')
    if len(keys[1]) != 2:
        raise Exception('must provide two numbers for checkboard')
    
    # Derive the internally used key from the input
    KEY = alphabetPermutation(keys[0])
    # Divide they KEY into a mutable list so we can pop from it
    KEY = [i for i in KEY]
    
    D = {}
    
    if decode == False:

        # First row of the checkerboard
        for i in range(10):
            if i not in keys[1]:
                D[KEY.pop(0)] = str(i)
        
        # Second row
        for i in range(10):
            codegroup = str(keys[1][0])+str(i)
            D[KEY.pop(0)] = codegroup

        # Third row   
        for i in range(8):
            codegroup = str(keys[1][1])+str(i)
            D[KEY.pop(0)] = codegroup

        return "".join([D[letter] for letter in text])
    
    if decode == True:
        # First row of the checkerboard
        for i in range(10):
            if i not in keys[1]:
                D[str(i)] = KEY.pop(0)
        
        # Second row
        for i in range(10):
            codegroup = str(keys[1][0])+str(i)
            D[codegroup] = KEY.pop(0)

        # Third row   
        for i in range(8):
            codegroup = str(keys[1][1])+str(i)
            D[codegroup] = KEY.pop(0)
        
        L = []
        text = [sym for sym in text]

        while len(text) > 0:
            if text[0] in str(keys[1]):
                L.append(text.pop(0)+text.pop(0))
            else:
                L.append(text.pop(0))
                
        return "".join([D[i] for i in L])





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


def DRYAD(text,key,decode=False,codepage=False):
    
    # Extend the text with zeroes so groups are all the same size
    while len(text) % 5 != 0:
        text += "0"
    
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





## Hill's matrix cipher is based on the fundamental operation of linear
## algebra, matrix multiplication. This is accomplished by dividing the text
## into chunks and using modular matrix multiplication to encrypt them. 

## Although the pure form of the cipher is not very secure it was one of the
## first serious block ciphers.

def modmatinv(M,n):
    d = int(det(M))
    i = modinv(d%n,n)
    
    invM = inv(M)*d*i
    invM = np.matrix.round(invM)
    invM = invM.astype(int)%n
    
    return invM

# The crudest possible method of creating keys. Pick a size and randomly
# generate matrices until one of them is truly invertible.
# It can take a while to generate a key if n is more than about 9.
def createMatrixKey(n):
    while True:
        M = np.matrix(np.random.randint(26, size=(n, n)))
        d = int(det(M))
        g,x,y = egcd(d%26,26)
        if g == 1:
            if np.all( M.dot(modmatinv(M,26))%26 == np.identity(n) ):
                return M
 
def hillCipher(text,key,decode=False):
    if decode == True:
        key = modmatinv(key,26)

    N = key.shape[0]

    b,rem = divmod(len(text),N)
    if rem != 0:
        text += "X"*(N-rem)

    out = ""
    for i in range(len(text)//N):
        x = [ord(j)-65 for j in text[i*N:N+i*N]]
        y = (x*key%26)+65
        out += "".join([chr(j) for j in y.flat])

    return out



def hillCipherExample():
    print("Example of the Hill Cipher\n")

    key = createMatrixKey(7)
    
    print("The key is \n{}\n".format(key))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = hillCipher(ptext,key)
    dtext = hillCipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

def DRYADexample():
    print("Example of the DRYAD Cipher\n")
    keys = random.getrandbits(64)
    print("The key is {}\n".format(keys))
    ptext = "213165587194201"
    ctext = DRYAD(ptext,keys)
    dtext = DRYAD(ctext,keys,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))


def straddlingCheckerboardExample():
    print("Example of the Straddling Checkerboard\n")
    keys = ["ZEBRA",[1,3]]
    print("The key is {}\n".format(keys))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = straddlingCheckerboard(ptext,keys)
    dtext = straddlingCheckerboard(ctext,keys,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#hillCipherExample()
#print("\n\n")
#DRYADexample()
#print("\n\n")
#straddlingCheckerboardExample()
    
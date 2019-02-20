from numpy import argsort
import random
from Ciphers.UtilityFunctions import uniqueRank, groups

## A transposition cipher is made by shuffling the letters of the message
## according to some rule. One of the most famous transposition ciphers is
## columnar transport. To do this the message is read into a matrix by rows
## then the columns of the matrix are suffled and read off by columns.

def columnarTransport(text,key,decode=False,complete=True):
    
    k = uniqueRank(key)
    
    ## Add nulls if necessary
    # The nulls are uncommon consonants so that they cannot accidentally form
    # words at the end of the true message
    numcol = len(k)
    numrow,rem = divmod(len(text),numcol)
    longCols = k[:rem]

    if complete == True:
        if rem != 0:
            nulls = numcol-rem
            text += "".join([random.choice(["Z","Q","J","X"]) for i in range(nulls)])
            numrow += 1
    
    if decode == True:

        
        ctr = 0
        L = []
        for i in range(numcol):
            if i in longCols:
                L.append(text[ctr:ctr+numrow+1])
                ctr += (numrow+1)
            else:
                L.append(text[ctr:ctr+numrow])
                ctr += numrow
        
        print(L)
        
        out = []
        
        for row in range(numrow+1):
            for col in k:
                if len(L[col]) > row:
                    out.append( L[col][row] )
        
        return "".join(out)
    
    if decode == False:
        
        # Read the text into the rows
        L = groups(text,len(k))

        # Read down each column
        out = []
        for col in argsort(k):
            for row in L:
                if len(row) > col:
                    out.append(row[col])
        return "".join(out)
    

    
## Double columnar transport is a significant improvement on the single columnar
## transport cipher. With long keys it is even somewhat resistant to computer attack.

def doubleColumnarTransport(text,key=["ABC","ABC"],decode=False):
    if len(key) != 2:
        raise Exception("Must have exactly two keys")
    while len(key[0]) > len(key[1]):
        key[1] += "Z"
    while len(key[1]) > len(key[0]):
        key[0] += "Z"
    if decode == True:
        return columnarTransport(columnarTransport(text,key[1],True),key[0],True)
    else:
        return columnarTransport(columnarTransport(text,key[0]),key[1])

    
def columnarTransportExample():

    print("Columnar Transport Example")
    key = "ILIKETHEEGGS"
    print("The Key Is {}".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = columnarTransport(ptext,key)
    dtext = columnarTransport(ctext,key,decode=True)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    print("Decodes As:\n{}".format(dtext))
    
def doubleColumnarTransportExample():

    print("Columnar Transport Example")
    keys = ["ILIKEEGGS","BLAHDIBLAHBLAH"]
    print("The Key Is {}".format(keys))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = doubleColumnarTransport(ptext,keys)
    dtext = doubleColumnarTransport(ctext,keys,decode=True)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    print("Decodes As:\n{}".format(dtext))

columnarTransportExample()
#doubleColumnarTransportExample()

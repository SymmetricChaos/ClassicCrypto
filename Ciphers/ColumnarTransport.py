from numpy import argsort
from numpy.random import choice
from Ciphers.UtilityFunctions import uniqueRank

## A transposition cipher is made by shuffling the letters of the message
## according to some rule. One of the most famous transposition ciphers is
## columnar transport. To do this the message is read into a matrix by rows
## then the columns of the matrix are suffled and read off by columns.

def columnarTransport(text,key,decode=False):
    
    k = uniqueRank(key)
    
    ## Add nulls if necessary
    # The nulls are uncommon consonants so that they cannot accidentally form
    # words at the end of the true message
    numcol = len(k)
    numrow,rem = divmod(len(text),numcol)
    if rem != 0:
        text += "".join(choice(["Z","Q","J","X","V","W"],numcol-rem))
        numrow += 1

    ## In case of decrypting
    if decode == True:
        L = []
        for i in range(numrow):
            L.append(text[i::numrow])
            
        out = ""
        for i in L:
            for j in k:
                out += i[j]
        
        return out 
    if decode == False:
        ## Create the rows
        L = []
        for i in range(numrow):
            L.append(text[i*numcol:numcol+i*numcol])
        
        ## Read the columns 
        out = ""
        for x in argsort(k):
            out += "".join([i[x] for i in L])
            
        return out
    
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
    key = "ILIKECHICKENEGGS"
    print("The Key Is {}".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = columnarTransport(ptext,key)
    dtext = columnarTransport(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
def doubleColumnarTransportExample():

    print("Columnar Transport Example")
    keys = ["ILIKEEGGS","BLAHDIBLAHBLAH"]
    print("The Key Is {}".format(keys))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = doubleColumnarTransport(ptext,keys)
    dtext = doubleColumnarTransport(ctext,keys,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
## A transposition cipher is made by shuffling the letters of the message
## according to some rule. One of the most famous transposition ciphers is
## columnar transport. To do this the message is read into a matrix by rows
## then the columns of the matrix are suffled and read off by columns.

## The order of the arguments
from numpy import argsort

def columnarTransport(text,key,decode=False):
    
    ## Add nulls if necessary
    numcol = len(key)
    numrow,rem = divmod(len(text),numcol)
    if rem != 0:
        text += "X"*(numcol-rem)
        numrow += 1

    ## In case of decrypting
    if decode == True:
        L = []
        for i in range(numrow):
            L.append(text[i::numrow])
            
        out = ""
        for i in L:
            for j in key:
                out += i[j]
        
        return out 
    if decode == False:
        ## Create the rows
        L = []
        for i in range(numrow):
            L.append(text[i*numcol:numcol+i*numcol])
        
        ## Read the columns 
        out = ""
        for x in argsort(key):
            out += "".join([i[x] for i in L])
            
        return out

### Double columnar transport is a significant improvement on the single columnar
### transport cipher. With long keys it is even somewhat resistant to computer attack.

def doubleColumnarTransport(text,key=[[0,1,2],[0,1,2]],decode=False):
    if len(key) != 2:
        raise Exception("Must have exactly two keys")
    if decode == True:
        return columnarTransport(columnarTransport(text,key[1],True),key[0],True)
    else:
        return columnarTransport(columnarTransport(text,key[0]),key[1])


#plaintext = "THECITYOFNEWYORKWASNAMEDAGYERTHEDUKEOFYORKINTHEYEAR1644ALTHOUGHITHADBEENSETTLEDLONGBEFORETHEEARLIESTKNOWNINHABITANTSLIVEDTHERE9000YEARSAGOINFACTTHOUSANDSOFSITESHAVEBEENFOUNDTHROUGHOUTTHECITYTHEMODERNWEKNOWTODAYWASCREATEDBYTHEDUTCHANDCALLEDNEWAMSTERDAMALARGEFORTRESSTHATSTILLEXISTSTODAYWASTHEHEARTOFTHECITYUNFORTUNATELYFORTHEDUTCHITWASEVENTUALLYCAPTUREDBYTHEBRITISHINTHEYEAR1664AYEARLATERTHOMASWILLETTBECAMETHE1STMAYORHEWOULDALSOBETHECITYSTHIRDMAYORIN1667XX"
#ctext = columnarTransport(plaintext,[5,3,4,1,2,0])
#print(ctext)
#decoded = columnarTransport(ctext,[5,3,4,1,2,0],decode=True)
#print("Decode Matches Plaintext:",decoded == plaintext)
#print(decoded)
#print()

#plaintext = "THECITYOFNEWYORKWASNAMEDAGYERTHEDUKEOFYORKINTHEYEAR1644ALTHOUGHITHADBEENSETTLEDLONGBEFORETHEEARLIESTKNOWNINHABITANTSLIVEDTHERE9000YEARSAGOINFACTTHOUSANDSOFSITESHAVEBEENFOUNDTHROUGHOUTTHECITYTHEMODERNWEKNOWTODAYWASCREATEDBYTHEDUTCHANDCALLEDNEWAMSTERDAMALARGEFORTRESSTHATSTILLEXISTSTODAYWASTHEHEARTOFTHECITYUNFORTUNATELYFORTHEDUTCHITWASEVENTUALLYCAPTUREDBYTHEBRITISHINTHEYEAR1664AYEARLATERTHOMASWILLETTBECAMETHE1STMAYORHEWOULDALSOBETHECITYSTHIRDMAYORIN1667XX"
#ctext = doubleColumnarTransport(plaintext,[5,3,4,1,2,0],[3,7,1,2,0,4,5,6])
#print(ctext)
#decoded = doubleColumnarTransport(ctext,[5,3,4,1,2,0],[3,7,1,2,0,4,5,6],decode=True)
#print("Decode Matches Plaintext:",decoded == plaintext)
#print(decoded)


# Some stuff we need for testing
from UtilityFunctions import decodetest
from PrepareText import preptext1

# Import the various ciphers
from RailfenceCipher import railfence
from ColumnarTransport import columnarTransport,doubleColumnarTransport

textfile = open('text1.txt', 'r')
ptext = preptext1(textfile.readline())

decodetest(ptext,[0,4,2,3,1],columnarTransport)

decodetest(ptext,[[0,4,2,3,1],[0,4,2,3,1]],doubleColumnarTransport)

decodetest(ptext,5,railfence)
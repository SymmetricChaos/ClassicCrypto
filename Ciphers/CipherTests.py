# Some stuff we need for testing
from UtilityFunctions import decodetest
from PrepareText import preptext1

# Import the various ciphers
from VigenereCipher import vigenere,multiVigenere,vigenereAutokey,affineVigenere
from Monoalphabetic import caesar,affine,substitution
from PolybiusSquare import polybiusSquare
from Nihilist import nihilistCipher
from StraddlingCheckerboard import straddlingCheckerboard
from RailfenceCipher import railfence
from ColumnarTransport import columnarTransport,doubleColumnarTransport


textfile = open('text1.txt', 'r')
ptext = preptext1(textfile.readline())

decodetest(ptext,1,caesar)

decodetest(ptext,[2,3],affine)

decodetest(ptext,"IOWNAXYLOPHONE",substitution)

decodetest(ptext,"THISISABOUTFARMING",vigenere)

decodetest(ptext,["THIS","IS","ABOUT","FARMING"],multiVigenere)

decodetest(ptext,"FARMING",vigenereAutokey)

decodetest(ptext,["SUGAR","CANE"],affineVigenere)

decodetest(ptext,"ZEBRAS",polybiusSquare)

decodetest(ptext,["NIHILIST","CIPHER"],nihilistCipher)

decodetest(ptext,["CIPHER",[5,7]],straddlingCheckerboard)

decodetest(ptext,[0,4,2,3,1],columnarTransport)

decodetest(ptext,[[0,4,2,3,1],[0,4,2,3,1]],doubleColumnarTransport)

decodetest(ptext,5,railfence)
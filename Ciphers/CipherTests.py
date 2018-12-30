# These tests are extremely simple and are used to confirm that decoding works
# properly.

# Some stuff we need for testing
from UtilityFunctions import decodetest
from PrepareText import preptext1
import numpy as np

# Import the various ciphers
from VigenereCipher import vigenere,multiVigenere,vigenereAutokey,affineVigenere
from Monoalphabetic import caesar,affine,substitution
from PolybiusSquare import polybiusSquare, nihilistCipher, ADFGVX, bifidCipher
from StraddlingCheckerboard import straddlingCheckerboard
from Transposition import columnarTransport,doubleColumnarTransport,railfence
from RotorMachines import rotorMachine
from HillMatrixCipher import hillCipher
from NomenclatorCipher import nomenclator

textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\text1.txt', 'r')
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

decodetest(ptext,["17ZEBRAS529",[1,4,2,5,0,3]],ADFGVX)

decodetest(ptext,"GIANTUNICORNS",bifidCipher)

decodetest(ptext,5766645,nomenclator)


R1 = "DMTWSILRUYQNKFEJCAZBPGXOHV"
R2 = "HQZGPJTMOBLNCIFDYAWVEUSRKX"
R3 = "UQNTLSZFMREHDPXKIBVYGJCWOA"
keySettings = [[R1,R2,R3],["R","F","W"],["AB","CD","XJ","ZY"]]
decodetest(ptext,keySettings,rotorMachine)



key = np.matrix([[12,14,24,4,6,4,13],
                [23,24,4,17,24,10,15],
                [17,0,18,6,22,22,11],
                [1,15,11,9,10,13,1],
                [9,9,16,9,18,24,6],
                [1,9,17,15,14,4,19],
                [24,20,5,0,15,21,12]])
decodetest(ptext,key,hillCipher)
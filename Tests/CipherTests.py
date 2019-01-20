# These tests are extremely simple and are used to confirm that decoding works
# properly.

# Some stuff we need for testing
from UtilityFunctions import decodetest, groups
from PrepareText import preptext1, playfairPrep
import numpy as np
import random

# Import the various ciphers
from VigenereCipher import vigenere,multiVigenere,vigenereAutokey,affineVigenere
from Monoalphabetic import caesar,affine,substitution
from OtherCiphers import hillCipher, straddlingCheckerboard
from PolybiusSquare import polybiusSquare, nihilistCipher, ADFGVX, bifidCipher,trifidCipher
from Transposition import columnarTransport,doubleColumnarTransport,railfence
from RotorMachines import enigma
from NomenclatorCipher import nomenclator
from Playfair import fourSquareCipher, playfairCipher
from Disks import cipherDisk, disruptedTableau, chaocipher

textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\text1.txt', 'r')
ptext = preptext1(textfile.readline())

# Monoalphabetic
decodetest(ptext,1,caesar)
decodetest(ptext,[2,3],affine)
decodetest(ptext,"IOWNAXYLOPHONE",substitution)

# Vigenere
decodetest(ptext,"THISISABOUTFARMING",vigenere)
decodetest(ptext,["THIS","IS","ABOUT","FARMING"],multiVigenere)
decodetest(ptext,"FARMING",vigenereAutokey)
decodetest(ptext,["SUGAR","CANE"],affineVigenere)

# Polybius Square
decodetest(ptext,"ZEBRAS",polybiusSquare)
decodetest(ptext,["NIHILIST","CIPHER"],nihilistCipher)
decodetest(ptext,["17ZEBRAS529",[1,4,2,5,0,3]],ADFGVX)
decodetest(ptext,"GIANTUNICORNS",bifidCipher)
decodetest(ptext,"GIANTUNICORNS",trifidCipher)

# Transposition
decodetest(ptext,[0,4,2,3,1],columnarTransport)
decodetest(ptext,[[0,4,2,3,1],[0,4,2,3,1]],doubleColumnarTransport)
decodetest(ptext,5,railfence)

# Disks
decodetest(ptext,"M0A8G7I4C3A2L6F4UNTI5MEL1AND",cipherDisk)
decodetest(ptext,"M0A8G7I4C3A2L6F4UNTI5MEL1AND",disruptedTableau)
decodetest(ptext,["",""],chaocipher)

# Codebook
decodetest(ptext,5766645,nomenclator)

# Playfair
ptextPlayfair = playfairPrep(ptext)
decodetest(ptextPlayfair,"ILIKEANTELOPES",playfairCipher)
decodetest(ptext,["4SQUARE2","10CODE7"],fourSquareCipher)

# Straddling Checkerboard
decodetest(ptext,["CIPHER",[5,7]],straddlingCheckerboard)


# Enigma Machine
rotors = random.sample(["I","II","III","IV","V"],k=3)
reflector = random.choice(["RA","RB","RC"])
positions = random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=3)
plugs = []
for i in groups(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=20),2):
    plugs.append("".join(i))
rings = ["A","A","A"]
keySettings = [rotors,reflector,positions,plugs,rings]
decodetest(ptext,keySettings,enigma)


# Hill Cipher
key = np.matrix([[12,14,24,4,6,4,13],
                [23,24,4,17,24,10,15],
                [17,0,18,6,22,22,11],
                [1,15,11,9,10,13,1],
                [9,9,16,9,18,24,6],
                [1,9,17,15,14,4,19],
                [24,20,5,0,15,21,12]])
decodetest(ptext,key,hillCipher)
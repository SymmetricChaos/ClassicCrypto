# These tests are extremely simple and are used to confirm that decoding works
# properly.

import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")

# Some stuff we need for testing
from Ciphers.UtilityFunctions import decodetest, preptext, playfairPrep

# Load up the text to use
textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\text1.txt', 'r')
ptext = preptext(textfile.readline())
print()

# Import the various ciphers
from Ciphers.Affine import affine
from Ciphers.Caesar import caesar
from Ciphers.Substitution import substitution
from Ciphers.Vigenere import vigenere, multiVigenere
from Ciphers.Beaufort import beaufort, multiBeaufort
from Ciphers.Autokey import autokey
from Ciphers.AffineVigenere import affineVigenere
from Ciphers.Polybius import polybiusSquare
from Ciphers.Nihilist import nihilist
from Ciphers.ADFGVX import ADFGVX
from Ciphers.Bifid import bifid
from Ciphers.Trifid import trifid
from Ciphers.ColumnarTransport import columnarTransport, doubleColumnarTransport
from Ciphers.Railfence import railfence
from Ciphers.CipherDisk import cipherDisk
from Ciphers.DisruptedTableau import disruptedTableau
from Ciphers.Chaocipher import chaocipher
from Ciphers.Nomenclator import nomenclator
from Ciphers.Playfair import playfair
from Ciphers.FourSquare import fourSquare
from Ciphers.StraddlingCheckerboard import straddlingCheckerboard
from Ciphers.Enigma import enigma
from Ciphers.HillCipher import hillCipher
from Ciphers.PrimeHillCipher import primeHillCipher
from Ciphers.TwoSquare import twoSquare

# Monoalphabetic
decodetest(ptext,1,caesar)
decodetest(ptext,[3,4],affine)
decodetest(ptext,"IOWNAXYLOPHONE",substitution)


# Vigenere
decodetest(ptext,"THISISABOUTFARMING",vigenere)
decodetest(ptext,["THIS","IS","ABOUT","FARMING"],multiVigenere)
decodetest(ptext,["THIS","IS","ABOUT","FARMING"],multiBeaufort)
decodetest(ptext,"FARMING",autokey)
decodetest(ptext,["SUGAR","CANE"],affineVigenere)
decodetest(ptext,"SUGARCANE",beaufort)


# Polybius Square
decodetest(ptext,"ZEBRAS",polybiusSquare)
decodetest(ptext,["NIHILIST","CIPHER"],nihilist)
decodetest(ptext,["17ZEBRAS529","GIGANTIC"],ADFGVX)
decodetest(ptext,"GIANTUNICORNS",bifid)
decodetest(ptext,"GIANTUNICORNS",trifid)


# Transposition
decodetest(ptext,"TABLES",columnarTransport)
decodetest(ptext,["GIGANTIC","TABLES"],doubleColumnarTransport)
decodetest(ptext,5,railfence)


# Disks
decodetest(ptext,"M0A8G7I4C3A2L6F4UNTI5MEL1AND",cipherDisk)
decodetest(ptext,"M0A8G7I4C3A2L6F4UNTI5MEL1AND",disruptedTableau)


# Playfair
ptextPlayfair = playfairPrep(ptext)
decodetest(ptextPlayfair,"ILIKEANTELOPES",playfair)
decodetest(ptext,["4SQUARE2","10CODE7"],fourSquare)
decodetest(ptext,["4SQUARE2","10CODE7"],twoSquare)


# Enigma Machine
rotors = ["V","III","II"]
reflector = "RB"
positions = ["H","L","B"]
plugs = ["AB","CD","EF","GH"]
rings = ["A","A","A"]
keySettings = [rotors,reflector,positions,plugs,rings]
decodetest(ptext,keySettings,enigma)


# Hill Cipher
key = [[12,14,24,4,6,4,13],
       [23,24,4,17,24,10,15],
       [17,0,18,6,22,22,11],
       [1,15,11,9,10,13,1],
       [9,9,16,9,18,24,6],
       [1,9,17,15,14,4,19],
       [24,20,5,0,15,21,12]]
decodetest(ptext,key,hillCipher)

key = [[5,10,25,24,19,1],
       [0,0,2,25,24,36],
       [6,1,29,12,17,16],
       [32,12,24,31,25,16],
       [15,12,26,23,12,37],
       [33,10,26,36,24,8]]
decodetest(ptext,key,primeHillCipher)


# Straddling Checkerboard
decodetest(ptext,["CIPHER",[5,7]],straddlingCheckerboard)


# Chaocipher
decodetest(ptext,["",""],chaocipher)


# Codebook
decodetest(ptext,5766645,nomenclator)
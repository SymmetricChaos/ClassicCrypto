# These tests are extremely simple and are used to confirm that decoding works
# properly.

import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")

# Some stuff we need for testing
from Ciphers.UtilityFunctions import decodetest
from Ciphers.PrepareText import preptext1, playfairPrep
import numpy as np

# Load up the text to use
textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\text1.txt', 'r')
ptext = preptext1(textfile.readline())

# Import the various ciphers
from Ciphers.Affine import affine
from Ciphers.Caesar import caesar
from Ciphers.Substitution import substitution
from Ciphers.Vigenere import vigenere
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

# Monoalphabetic
decodetest(ptext,1,caesar)
decodetest(ptext,[2,3],affine)
decodetest(ptext,"IOWNAXYLOPHONE",substitution)


# Vigenere
decodetest(ptext,"THISISABOUTFARMING",vigenere)
decodetest(ptext,"FARMING",autokey)
decodetest(ptext,["SUGAR","CANE"],affineVigenere)


# Polybius Square
decodetest(ptext,"ZEBRAS",polybiusSquare)
decodetest(ptext,["NIHILIST","CIPHER"],nihilist)
decodetest(ptext,["17ZEBRAS529",[1,4,2,5,0,3]],ADFGVX)
decodetest(ptext,"GIANTUNICORNS",bifid)
decodetest(ptext,"GIANTUNICORNS",trifid)


# Transposition
decodetest(ptext,[0,4,2,3,1],columnarTransport)
decodetest(ptext,[[0,4,2,3,1],[0,4,2,3,1]],doubleColumnarTransport)
decodetest(ptext,5,railfence)


# Disks
decodetest(ptext,"M0A8G7I4C3A2L6F4UNTI5MEL1AND",cipherDisk)
decodetest(ptext,"M0A8G7I4C3A2L6F4UNTI5MEL1AND",disruptedTableau)


# Playfair
ptextPlayfair = playfairPrep(ptext)
decodetest(ptextPlayfair,"ILIKEANTELOPES",playfair)
decodetest(ptext,["4SQUARE2","10CODE7"],fourSquare)


# Enigma Machine
rotors = ["V","III","II"]
reflector = "RB"
positions = ["H","L","B"]
plugs = ["AB","CD","EF","GH"]
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


# Straddling Checkerboard
decodetest(ptext,["CIPHER",[5,7]],straddlingCheckerboard)


# Chaocipher
decodetest(ptext,["",""],chaocipher)


# Codebook
decodetest(ptext,5766645,nomenclator)
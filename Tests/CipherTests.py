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

from Ciphers.Vigenere import vigenere, multiVigenere, trithemius
from Ciphers.Beaufort import beaufort, multiBeaufort
from Ciphers.Autokey import autokey
from Ciphers.AffineVigenere import affineVigenere
from Ciphers.Quagmire import quagmire1, quagmire2, quagmire3, quagmire4

from Ciphers.Playfair import playfair
from Ciphers.TwoSquare import twoSquare
from Ciphers.FourSquare import fourSquare

from Ciphers.Polybius import polybiusSquare
from Ciphers.Nihilist import nihilist
from Ciphers.ADFGVX import ADFGVX
from Ciphers.Bifid import bifid
from Ciphers.Trifid import trifid

from Ciphers.CipherDisk import cipherDisk

from Ciphers.Nomenclator import nomenclator

from Ciphers.StraddlingCheckerboard import straddlingCheckerboard

from Ciphers.HillCipher import hillCipher

from Ciphers.Chaocipher import chaocipher
from Ciphers.Hutton import hutton

from Ciphers.AMSCO import AMSCO
from Ciphers.ColumnarTransport import columnarTransport, doubleColumnarTransport
from Ciphers.Railfence import railfence

from Ciphers.Enigma import enigma
from Ciphers.SIGABA import SIGABA
from Ciphers.M209 import M209

# Monoalphabetic
decodetest(ptext,1,caesar)
decodetest(ptext,[3,4],affine)
decodetest(ptext,"IOWNAXYLOPHONE",substitution)

# Vigenere
decodetest(ptext,"THISISABOUTFARMING",vigenere)
decodetest(ptext,"SUGARCANE",beaufort)
decodetest(ptext,["THIS","IS","ABOUT","FARMING"],multiVigenere)
decodetest(ptext,["THIS","IS","ABOUT","FARMING"],multiBeaufort)
decodetest(ptext,"FARMING",autokey)
decodetest(ptext,["SUGAR","CANE"],affineVigenere)
decodetest(ptext,"",trithemius)


# Polybius Square
decodetest(ptext,"ZEBRAS",polybiusSquare)
decodetest(ptext,["NIHILIST","CIPHER"],nihilist)
decodetest(ptext,["17ZEBRAS529","GIGANTIC"],ADFGVX)
decodetest(ptext,"GIANTUNICORNS",bifid)
decodetest(ptext,"GIANTUNICORNS",trifid)

# Quagmire Ciphers
decodetest(ptext,["FLYING","ZEBRA"],quagmire1)
decodetest(ptext,["FLYING","ZEBRA"],quagmire2)
decodetest(ptext,["FLYING","ZEBRA"],quagmire3)
decodetest(ptext,["FLYING","ZEBRA","CAVALRY"],quagmire4)

# Chaocipher
decodetest(ptext,["",""],chaocipher)

# Hutton Cipher
decodetest(ptext,["JUPTIER","FEDROA"],hutton)

# Disks
decodetest(ptext,"M0A8G7I4C3A2L6F4UNTI5MEL1AND",cipherDisk)

# Playfair
ptextPlayfair = playfairPrep(ptext)
decodetest(ptextPlayfair,"ILIKEANTELOPES",playfair)
decodetest(ptext,["4SQUARE2","10CODE7"],fourSquare)
decodetest(ptext,["4SQUARE2","10CODE7"],twoSquare)


# Enigma Machine
rotors =    ["V","III","II"]
reflector = "B"
positions = ["H","L","B"]
plugs =     ["AB","CD","EF","GH"]
rings =     ["A","A","A"]
keySettings = [rotors,reflector,positions,plugs,rings]
decodetest(ptext,keySettings,enigma)

# SIGABA
cipher =     ["IV","X","VII","III","II"]
control =    ["IX","V","I","VI","VIII"]
index =      ["II","IV","V","I","III"]
indicator =  "HUPYU"
controlPos = "JBKPO"
indexPos =   "02384"
keySettings = [cipher,control,index,indicator,controlPos,indexPos]
SIGtext = ptext
SIGtext = SIGtext.replace("Z","X")
decodetest(SIGtext,keySettings,SIGABA)

# M209
pins = ["++-+---++-+-++----++-++---",
        "+--++-+--+++--+--++-+-+--",
        "++----++-+-+++---++++-+",
        "--+-++-++---++-+--+++",
        "-+-+++-++---++-+--+",
        "++-+---+--+--++-+"]
lugs = [[3,6], [0,6], [1,6], [1,5], [4,5], [0,4], [0,4],
        [0,4], [0,4], [2,0], [2,0], [2,0], [2,0], [2,0],
        [2,0], [2,0], [2,0], [2,0], [2,0], [2,5], [2,5],
        [0,5], [0,5], [0,5], [0,5], [0,5], [0,5]]
decodetest(ptext,["TABLEA",pins,lugs],M209)

# Hill Cipher
key = [[12,14,24,4,6,4,13],
       [23,24,4,17,24,10,15],
       [17,0,18,6,22,22,11],
       [1,15,11,9,10,13,1],
       [9,9,16,9,18,24,6],
      [1,9,17,15,14,4,19],
       [24,20,5,0,15,21,12]]
decodetest(ptext,key,hillCipher)


# Straddling Checkerboard
decodetest(ptext,["CIPHER",[5,7]],straddlingCheckerboard)

# Codebook
decodetest(ptext,5766645,nomenclator)


# Transposition
decodetest(ptext,"TABLES",columnarTransport)
decodetest(ptext,["GIGANTIC","TABLES"],doubleColumnarTransport)
decodetest(ptext,5,railfence)
decodetest(ptext,"GIGANTIC",AMSCO)
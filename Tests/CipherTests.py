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
from Ciphers import affine
from Ciphers import caesar
from Ciphers import substitution

from Ciphers import vigenere, multiVigenere, trithemius
from Ciphers import beaufort, multiBeaufort
from Ciphers import autokey
from Ciphers import affineVigenere
from Ciphers import quagmire1, quagmire2, quagmire3, quagmire4

from Ciphers import playfair
from Ciphers import twoSquare
from Ciphers import fourSquare

from Ciphers import polybiusSquare
from Ciphers import nihilist
from Ciphers import ADFGVX
from Ciphers import bifid
from Ciphers import trifid

from Ciphers import cipherDisk

from Ciphers import nomenclator

from Ciphers import straddlingCheckerboard

from Ciphers import hillCipher

from Ciphers import chaocipher
from Ciphers import hutton

from Ciphers import AMSCO
from Ciphers import columnarTransport, doubleColumnarTransport
from Ciphers import railfence

from Ciphers import enigma
from Ciphers import SIGABA
from Ciphers import M209

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
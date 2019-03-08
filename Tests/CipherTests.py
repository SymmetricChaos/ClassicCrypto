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

# Monoalphabetic substitution
#from Ciphers import affine, caesar, substitution
from Ciphers.Simple import affine, caesar, substitution

# Variation on the Vigenere cipher
from Ciphers import vigenere, multiVigenere, trithemius, beaufort, \
                    multiBeaufort, autokey, affineVigenere, \
                    quagmire1, quagmire2, quagmire3, quagmire4

# Variation on the Playfair Cipher
from Ciphers import playfair, twoSquare, fourSquare

# Variations on the polybius square
from Ciphers import polybiusSquare, nihilist, ADFGX, ADFGVX, bifid, trifid

# Transposition ciphers
from Ciphers import AMSCO, columnarTransport, doubleColumnarTransport, railfence, turningGrille

# Rotor machines
from Ciphers import enigma, SIGABA, M209

# Mutating alphabet ciphers
from Ciphers import chaocipher, hutton

# Everything else
from Ciphers import cipherDisk, nomenclator, straddlingCheckerboard, hillCipher



decodetest(ptext,1,caesar)
decodetest(ptext,[3,4],affine)
decodetest(ptext,"IOWNAXYLOPHONE",substitution)

decodetest(ptext,"THISISABOUTFARMING",vigenere)
decodetest(ptext,"SUGARCANE",beaufort)
#decodetest(ptext,["THIS","IS","ABOUT","FARMING"],multiVigenere)
#decodetest(ptext,["THIS","IS","ABOUT","FARMING"],multiBeaufort)
decodetest(ptext,"FARMING",autokey)
decodetest(ptext,["SUGAR","CANE"],affineVigenere)
decodetest(ptext,"",trithemius)

decodetest(ptext,"ZEBRAS",polybiusSquare)
decodetest(ptext,["NIHILIST","CIPHER"],nihilist)
decodetest(ptext.replace("J","I"),["ZEBRAS","GIGANTIC"],ADFGX)
decodetest(ptext,["17ZEBRAS529","GIGANTIC"],ADFGVX)
decodetest(ptext,"GIANTUNICORNS",bifid)
decodetest(ptext,"GIANTUNICORNS",trifid)

decodetest(ptext,["FLYING","ZEBRA"],quagmire1)
decodetest(ptext,["FLYING","ZEBRA"],quagmire2)
decodetest(ptext,["FLYING","ZEBRA"],quagmire3)
decodetest(ptext,["FLYING","ZEBRA","CAVALRY"],quagmire4)

decodetest(ptext,["",""],chaocipher)
decodetest(ptext,["JUPTIER","FEDROA"],hutton)

decodetest(ptext,"M0A8G7I4C3A2L6F4UNTI5MEL1AND",cipherDisk)

decodetest(playfairPrep(ptext),"ILIKEANTELOPES",playfair)
decodetest(ptext,["4SQUARE2","10CODE7"],fourSquare)
decodetest(ptext,["4SQUARE2","10CODE7"],twoSquare)

rotors =    ["V","III","II"]
reflector = "B"
positions = ["H","L","B"]
plugs =     ["AB","CD","EF","GH"]
rings =     ["A","A","A"]
keySettings = [rotors,reflector,positions,plugs,rings]
decodetest(ptext,keySettings,enigma)

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

key = [[12,14,24,4,6,4,13],
       [23,24,4,17,24,10,15],
       [17,0,18,6,22,22,11],
       [1,15,11,9,10,13,1],
       [9,9,16,9,18,24,6],
      [1,9,17,15,14,4,19],
       [24,20,5,0,15,21,12]]
decodetest(ptext,key,hillCipher)

decodetest(ptext,["CIPHER",[5,7]],straddlingCheckerboard)

decodetest(ptext,5766645,nomenclator)

decodetest(ptext,"TABLES",columnarTransport)
decodetest(ptext,["GIGANTIC","TABLES"],doubleColumnarTransport)
decodetest(ptext,5,railfence)
decodetest(ptext,"GIGANTIC",AMSCO)
decodetest(ptext[:144],[i for i in range(36)],turningGrille,N=6)
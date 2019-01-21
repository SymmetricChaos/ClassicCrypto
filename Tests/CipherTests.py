# These tests are extremely simple and are used to confirm that decoding works
# properly.

import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")

# Some stuff we need for testing
from Ciphers.UtilityFunctions import decodetest
from Ciphers.PrepareText import preptext1, playfairPrep
import numpy as np
import random

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
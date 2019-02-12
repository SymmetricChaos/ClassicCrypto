import random
from Codes.MorseCode import binaryMorseCode
from Codes.PrefixCode import prefixCode
from Codes.BaconCode import baconCode
from Codes.Braille import binaryBraille

# The so-called Bacon cipher is really nothing of the sort. Rather it is a way
# of hiding a binary code in another piece of text. Bacon developed a specific
# encoding for this but any of them can be used.

def baconCipher(text,code,stegotext="",decode=False):
    
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWER = "abcdefghijklmnopqrstuvwxyz"

    
    if decode == False:
        ctext = code(text)
    
        # If using the stegotext option there has to be enough text
        if stegotext != "":
            if len(stegotext) < len(ctext):
                raise Exception('at least {} false test characters needed'.format(len(ctext)))

        out = ""
        # If not using any stegotext random letters are picked
        if stegotext == "":
            for bit in ctext:
                if bit == "0":
                    out += random.choice(LOWER)
                if bit == "1":
                    out += random.choice(UPPER)
        else:
            for L1,L2 in zip(ctext,stegotext):
                if L1 == "0":
                    out += L2.lower()
                if L1 == "1":
                    out += L2.upper()

        return out
    
    if decode == True:
        dtext = ""
        for letter in text:
            if letter.islower():
                dtext += "0"
            if letter.isupper():
                dtext += "1"
        
        out = code(dtext,decode=True)
            
        return out
    
def baconCipherExample():
    print("Example of the Bacon Cipher\n\n")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    for codeType in [prefixCode,baconCode,binaryMorseCode,binaryBraille]:
        print("Using {}:\n".format(codeType.__name__))
        ctext = baconCipher(ptext,codeType)
        dtext = baconCipher(ctext,codeType,decode=True)
        print(ptext)
        print(ctext)
        if ptext == dtext:
            print("\n(Decode Works)")
        else:
            print("\n(Decode Failed)")
        print("\n")
        
#baconCipherExample()
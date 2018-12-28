# The so-called Bacon Cipher is actually a simple code that is well suited to 
# being hidden. This implementation hides the code as uppercase and lower case 
# letters.

import random
from UtilityFunctions import groups

def baconCipher(text,stegotext="",decode=False):
    
    # If using the stegotext option there has to be enough text
    if stegotext != "":
        if len(stegotext) < len(text)*5:
            raise Exception('not enough stegotext provided')
        
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWER = "abcdefghijklmnopqrstuvwxyz"
    codes = ["00000","00001","00010","00011","00100","00101","00110","00111",
             "01000","01001","01010","01011","01100","01101","01110","01111",
             "10000","10001","10010","10011","10100","10101","10110","10111",
             "11000","11001"]
    
    if decode == False:
        out = []
        # If not using any stegotext random letters are picked
        if stegotext == "":
            for letter in text:
                code = codes[UPPER.index(letter)]
                
                for bit in code:
                    if bit == "0":
                        out.append(random.choice(LOWER))
                    if bit == "1":
                        out.append(random.choice(UPPER))
        else:
            ctr = 0
            for letter in text:
                code = codes[UPPER.index(letter)]
                
                for bit in code:
                    if bit == "0":
                        out.append(stegotext[ctr].lower())
                    if bit == "1":
                        out.append(stegotext[ctr].upper()) 
                    ctr += 1

        return "".join(out)
    
    if decode == True:
        out = ""
        for letters in groups(text,5):
            code = ""
            for bit in letters:
                if bit.islower():
                    code += "0"
                if bit.isupper():
                    code += "1"
            out += UPPER[codes.index(code)]
        return out

ctext = baconCipher("THEQUICK","thisisasomewhatlongpieceoftextthatityped")
dtext = baconCipher(ctext,decode=True)
print(ctext)
print(dtext)

print()

ctext = baconCipher("THEQUICK")
dtext = baconCipher(ctext,decode=True)
print(ctext)
print(dtext)

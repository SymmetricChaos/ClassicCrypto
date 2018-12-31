

# Morse code is a very popular method of encoding letters and numbers
# variations exist for languages other than English.

import random
from UtilityFunctions import groups


def morseCode(text,decode=False):
    if "." in text or "-" in text:
        if decode == False:
            raise Exception('text contains dots and dashes')
    
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    M = [".- ","-... ","-.-. ","-.. ",". ","..-. ","--. ",".... ",
         ".. ",".--- ","-.- ",".-.. ","-- ","-. ","--- ",".--. ",
         "--.- ",".-. ","... ","- ","..- ","...- ",".-- ","-..- ",
         "-.-- ","--.. ","----- ",".---- ","..--- ","...-- ",
         "....- ","..... ","-.... ","--... ","---.. ","----. "]

    D = {}
    
    if decode == False:
        for a,m in zip(A,M):
            D[a] = m
        
        out = [D[letter] for letter in text]
        
        return "".join(out)
            
        
    if decode == True:
        for a,m in zip(A,M):
            D[m] = a
        
        text = text.split(" ")
        
        # If there are any trailing spaces remove them
        while text[-1] == " " or text[-1] == "":
            text.pop()

        out = [D[code+" "] for code in text]
        
        return "".join(out)

    


# The so-called Bacon Cipher is actually a simple code that is well suited to 
# being hidden. This implementation hides the code as uppercase and lower case 
# letters.


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

# A prefix code is any code in which words can be of various lengths but which
# does not need commas to show the breaks between them. There are many ways to
# accomplish this. This example uses the Fibonnaci numbers. To keep the encoded
# text as short as possible short codes are given to common letters. However it
# is still not especially compact.

# Of interest for classical cryptopgrahy is that a variable length encoding can
# disguised the actual length of the message.

# Lagged fibonnaci numbers the sequence starts: 1,2,3,5,8,11
def fibonnaci(n):
    a = 1
    b = 1
    out = []
    for i in range(n):
        out.append(a)
        a,b = a+b,a
    return out

# There has to be a better way to do this, right?
# Go through the list for the first few Fibonnaci numbers from greatest to
# make a list of Fibonnaci numbers that add up to each code number (1,2,3...)
# The code is then the indexes of those Fibonnaci numbers, with leading zeroes
# removed, reversed, with an additional "1" at the end.
def makeCodebook(decode=False):
    F = fibonnaci(10)
    F.reverse()
    codes = []
    for x in range(1,27):
        while x != 0:
            code = []
            for f in F:
                if f <= x:
                    code.append("1")
                    x = x-f
                else:
                    code.append("0")

            while code[0] == "0":

                code.pop(0)
            code.reverse()
            code.append("1")
            codes.append("".join(code))
            
    # Matchup codes with letters
    D = {}
    alpha = "ETAOINSRHLDCUMFPGWYBVKXJQZ"
    if decode == False:
        for a,b in zip(alpha,codes):
            D[a] = b
            
    if decode == True:
        for a,b in zip(alpha,codes):
            D[b] = a
    return D
    
def prefixCode(text,decode=False):
    
    # Build the codebook
    D = makeCodebook(decode=decode)
    
    # When encoding we simply translate each letter to its code
    if decode == False:
        out = []
        for letter in text:
            out.append(D[letter])
        return "".join(out)
    
    # When decoding we put the bits into a buffer one at a time until it
    # matches a code. Once it matches we record the letter and then we clear
    # the buffer.
    if decode == True:
        out = []
        bits = [b for b in text]
        code = ""
        while len(bits) > 0:
            code += bits.pop(0)[0]
            if code in list(D.keys()):
                out.append(D[code])
                code = ""
        return "".join(out)
       
        
#ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
#ctext = morseCode(ptext)
#dtext = morseCode(ctext,decode=True)
#print(ctext)
#print(dtext)

#ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
#ctext = prefixCode(ptext)
#dtext = prefixCode(ctext,decode=True)

#print(ptext)
#print(ctext)
#print(dtext)

#ctext = baconCipher("THEQUICK","thisisasomewhatlongpieceoftextthatityped")
#dtext = baconCipher(ctext,decode=True)
#print(ctext)
#print(dtext)

#print()

#ctext = baconCipher("THEQUICK")
#dtext = baconCipher(ctext,decode=True)
#print(ctext)
#print(dtext)

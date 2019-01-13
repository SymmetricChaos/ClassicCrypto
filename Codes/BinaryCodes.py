import random
from UtilityFunctions import groups

# Morse code is a very popular method of encoding letters and numbers. It is
# not technically a binary code since it requires dots, dashes, and spaces in
# order to be interpreted.

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
    

# We can turn Morse code into a true binary code by representing the current on
# the line directly. 

def binaryMorseCode(text,decode=False):
    if decode == False:
        ctext = morseCode(text)
        ctext = ctext.replace("-","110")
        ctext = ctext.replace(".","10")
        ctext = ctext.replace(" ","00")
        return ctext
    
    if decode == True:
        text = text.replace("11","-")
        text = text.replace("1",".")
        text = text.replace("00"," ")
        text = text.replace("0","")
        
        return morseCode(text,decode=True)



# A prefix code is any code in which words can be of various lengths but which
# does not need commas to show the breaks between them. There are many ways to
# accomplish this. This example uses the fibonacci numbers. To keep the encoded
# text as short as possible short codes are given to common letters. However it
# is still not especially compact.

# Of interest for classical cryptopgrahy is that a variable length encoding can
# disguised the actual length of the message.

# Lagged fibonacci numbers the sequence starts: 1,2,3,5,8,11
def fibonacci(n):
    a = 1
    b = 1
    out = []
    for i in range(n):
        out.append(a)
        a,b = a+b,a
    return out

# There has to be a better way to do this, right?
# Go through the list for the first few fibonacci numbers from greatest to
# make a list of fibonacci numbers that add up to each code number (1,2,3...)
# The code is then the indexes of those fibonacci numbers, with leading zeroes
# removed, reversed, with an additional "1" at the end.
def makeCodebook(decode=False):
    F = fibonacci(10)
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
    
# Usually called the "Bacon Cipher" this is really a simple binary code. Every
# letter is represented by a five bit code. This would allow for thirty two
# characters, though only 26 are used. The next section adapted Bacon's method
# of stegonography to any binary code.
def baconCode(text,decode=False):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    codes = ["00000","00001","00010","00011","00100","00101","00110","00111",
             "01000","01001","01010","01011","01100","01101","01110","01111",
             "10000","10001","10010","10011","10100","10101","10110","10111",
             "11000","11001"]
    
    if decode == False:
        out = ""
        for letter in text:
            out += codes[letters.index(letter)]

        return out
    
    if decode == True:
        out = ""
        for code in groups(text,5):
            out += letters[codes.index(code)]
        return out
    
# The so-called Bacon Cipher is actually a simple code that is well suited to 
# being hidden. This implementation hides the code as uppercase and lower case 
# letters.


def baconCipher(text,code,stegotext="",decode=False):
    
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWER = "abcdefghijklmnopqrstuvwxyz"

    
    if decode == False:
        ctext = code(text)
    
        # If using the stegotext option there has to be enough text
        if stegotext != "":
            if len(stegotext) < len(ctext):
                raise Exception('not enough stegotext provided')

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
       
def morseCodeExample():
    print("Example of Morse Code\n")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = morseCode(ptext)
    print(ptext)
    print(ctext)

def binaryMorseCodeExample():
    print("Example of Binary Morse Code\n")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = binaryMorseCode(ptext)
    print(ptext)
    print(ctext)

def prefixCodeExample():
    print("Example of a Fibonacci Prefix Code\n")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = prefixCode(ptext)
    print(ptext)
    print(ctext)
    
def baconCodeExample():
    print("Example of the Bacon Code\n")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = baconCode(ptext)
    print(ptext)
    print(ctext)
    
def baconCipherExample():
    print("Example of the Bacon Cipher\n\n")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    for codeType in [prefixCode,baconCode,binaryMorseCode]:
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

#morseCodeExample()
#print()
#binaryMorseCodeExample()
#print()
#prefixCodeExample()
#print()
#baconCodeExample()
#print()
#baconCipherExample()
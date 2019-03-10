from Ciphers.UtilityFunctions import validptext

# Morse code is a very popular method of encoding letters and numbers. It is
# not technically a binary code since it requires dots, dashes, and spaces in
# order to be interpreted.

def morseCode(text,decode=False):
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    M = [".- ","-... ","-.-. ","-.. ",". ","..-. ","--. ",".... ",
         ".. ",".--- ","-.- ",".-.. ","-- ","-. ","--- ",".--. ",
         "--.- ",".-. ","... ","- ","..- ","...- ",".-- ","-..- ",
         "-.-- ","--.. ","----- ",".---- ","..--- ","...-- ",
         "....- ","..... ","-.... ","--... ","---.. ","----. "]


    validptext(text,A)

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
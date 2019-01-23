from Codes.UtilityFunctions import groups

# This fixed length encoding encoding was developed by Francis Bacon

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
    
def baconCodeExample():
    print("Example of the Bacon Code\n")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = baconCode(ptext)
    print(ptext)
    print(ctext)
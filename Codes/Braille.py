from Ciphers.UtilityFunctions import groups

def braille(text,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    braille =["\u2801","\u2803","\u2809","\u2819","\u2811",
              "\u280B","\u281B","\u2813","\u280A","\u281A",
              "\u2805","\u2807","\u280D","\u281D","\u2815",
              "\u280F","\u281F","\u2817","\u280E","\u281E",
              "\u2825","\u2827","\u283A","\u282D","\u283D",
              "\u2835"]
    
    D = {}
    if decode == False:
        for i,j in zip(alpha,braille):
            D[i] = j
            
        out = ""
        for i in text:
            out += D[i]
        
        return out
    
    if decode == True:
        for i,j in zip(alpha,braille):
            D[j] = i
        
        out = ""
        for i in text:
            out += D[i]
        
        return out


# Every Braille symbol consists of six dots that can be either raised or not
# raised. That allows it to be written as a six bit binary code.
# There is also an eight bit extended version but it is not as standardized.
def binaryBraille(text,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    braille =["010000", "100000", "101000", "110000", 
              "110100", "100100", "111000", "111100", 
              "101100", "011000", "011100", "100010", 
              "101010", "110010", "110110", "100110", 
              "111010", "111110", "101110", "011010", 
              "011110", "100011", "101011", "011101", 
              "110011", "110111", "100111"]
    D = {}
    if decode == False:
        for i,j in zip(alpha,braille):
            D[i] = j
            
        out = ""
        for i in text:
            out += D[i]
        
        return out
    
    if decode == True:
        for i,j in zip(alpha,braille):
            D[j] = i
        
        out = ""
        for i in groups(text,6):
            out += D[i]
        
        return out
        
    
def brailleExample():
    print("Example of Braille\n")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = braille(ptext)
    print(ptext)
    print(ctext)
    
def binaryBrailleExample():
    print("Example of Braille\n")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = binaryBraille(ptext)
    print(ptext)
    print(ctext)
    
#brailleExample()
#binaryBrailleExample()
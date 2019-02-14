# https://people.duke.edu/~ng46/collections/evans-basic-english-1947.pdf

from Ciphers.UtilityFunctions import preptext

# This brevity code is based on the Evans Basic English Code which makes two
# kinds of changes. First it replaces long common words with shorter versions
# and then it looks for suffixes that commonly appear and replaces those. The
# resulting replacements are meant to still be understanable to a native
# English speaker. However this system is not guaranteed to be easy to read. It
# is necessary to check that the output makes sense.

# Brevity codes are not a form of encryption in and of themselves but they are
# extremely useful in classical encryption because they make the plaintext
# much harder to analyze. Messages are shorter and lack some of their most
# distinctive patterns of letters.

def suffixCodes(text,exceptions=[]):
        
    suffs = ['ABILITY', 'IBILITY', 'ACTORY', 'ATIVE', 'FULLY', 'OLOGY', 'ILITY', 'ATION',
             'ATORY', 'ITIES', 'AZITE', 'ITION', 'ITIVE', 'IVELY', 'ULOUS', 'ENCY', 'SION',
             'HOOD', 'NESS', 'IOUS', 'MENT', 'ABLE', 'WARD', 'LESS', 'SELF', 'IBLE', 'SOME',
             'SHIP', 'STER', 'IEST', 'ANCY', 'ICAL', 'ATIC', 'ENCE', 'ANCE', 'IBLY', 'ABLY',
             'ALLY', 'TIVE', 'TION', 'AGE', 'BLE', 'IFY', 'ISH', 'OUS', 'ING', 'UAL', 'FUL',
             'IED', 'ACY', 'ISE', 'IAL', 'ILY', 'YZE', 'IST', 'ANT', 'IES', 'ATE', 'URE', 'ENT',
             'ORY', 'ERY', 'ITE', 'ARY', 'IVE', 'EER', 'ETY', 'ITY', 'IAN', 'IZE', 'ISM', 'LTY',
             'EST', 'IC', 'AL', 'ES', 'ED', 'ND', 'EE', 'LY', 'ER', 'OR', 'TH', 'RD', 'OON']
                
    suffCodes = ['BY', 'BY', 'RY', 'V', 'FY', 'GY', 'LY', 'N', 'RY', 'TS', 'TZ', 'N', 'V', 'VY', 'X',
             'CY', 'N', 'HD', 'NS', 'X', 'M', 'L', 'WD', 'LS', 'F', 'L', 'SM', 'SP', 'SR', 'ST', 'CY',
             'CL', 'C', 'C', 'C', 'BY', 'BY', 'LY', 'V', 'N', 'J', 'L', 'FY', 'H', 'X', 'G', 'L', 'F',
             'D', 'CY', 'Z', 'L', 'LY', 'Z', 'ST', 'T', 'S', 'T', 'U', 'T', 'RY', 'RY', 'T', 'RY', 'V',
             'R', 'TY', 'TY', 'N', 'Z', 'M', 'LY', 'ST', 'C', 'L', 'S', 'D', 'D', 'E', 'Y', 'R', 'R',
             'H', 'D', 'N']

    # Any words noted as exceptions are marked with an asterisk to prevent them
    # from being changed.
    for word in exceptions:
        text = text.replace(" {} ".format(word)," {}* ".format(word))
    
        # If any suffix appears as a complete word like ED or AGE we mark it with
    # an asterisk to prevent it being changed.
    for j in suffs:
        text = text.replace(" {} ".format(j)," {}* ".format(j))
    
    # Replace suffices with codes and also an asterisk to prevent it from being
    # modified again.
    for i,j in zip(suffCodes,suffs):
        text = text.replace(j + " ", i + "* ")

    # Get rid of the asterisks.
    text = text.replace("*", "")

    return text

def wordCode(text,exceptions=[]):
    
    # Replace common words with abbreviations
    words = ['DIFFERENT','BECAUSE','ABOUT','PEOPLE','BETWEEN','WOULD','SHOULD','COULD',
             'GOVERNMENT','IMPORTANT', 'YOU', 'ARE']
    wordCodes = ['DIFF','BC','ABT','PPL','BTWN','WLD','SHLD','CLD','GOVT','IMPT', 'U',
                 'R']

    # Any words noted as exceptions are marked with an asterisk to prevent them
    # from being changed.
    for word in exceptions:
        text = text.replace(" {} ".format(word)," {}* ".format(word))
    
    # Replace common words with codes and also an asterisk to prevent it from 
    # being modified again.
    for i,j in zip(wordCodes,words):
        text = text.replace(" " + j + " ", " " + i + "* ")

    # Get rid of the asterisks.
    text = text.replace("*", "")

    return text
    

def wordCodeExample():
    
    textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\Text3.txt', 'r')
    ptext = ""
    for i in textfile.readlines():
        ptext += preptext(i,keepSpaces=True,silent=True) + " "
        
    ptext = ptext[:1113]
    print("\n")
    print(ptext)
    print(len(ptext))
    print("\n")
    ctext = wordCode(ptext)
    print(ctext)
    print(len(ctext))
    
def suffixCodeExample():
    
    textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\Text3.txt', 'r')
    ptext = ""
    for i in textfile.readlines():
        ptext += preptext(i,keepSpaces=True,silent=True) + " "
        
    ptext = ptext[:1113]
    print("\n")
    print(ptext)
    print(len(ptext))
    print("\n")
    ctext = suffixCodes(ptext)
    print(ctext)
    print(len(ctext))
    
    
#brevityCodeExample()
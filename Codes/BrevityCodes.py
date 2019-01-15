# https://people.duke.edu/~ng46/collections/evans-basic-english-1947.pdf

from PrepareText import preptext3

# Brevity codes are not a form of encryption in and of themselves but they are
# extremely useful in classical encryption because they make the plaintext
# much harder to analyze. Messages are shorter and lack some of their most
# distinctive patterns of letters.

# This brevity code is a version of the Phillips code that changes the suffixes
# of words to something shorter.

textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\WindyHill.txt', 'r')
ptext = preptext3(textfile.readline())


def suffixes(text):
    suffs = ['ABILITY', 'IBILITY', 'ACTORY', 'ATIVE', 'FULLY', 'OLOGY', 'ILITY', 'ATION',
             'ATORY', 'ITIES', 'AZITE', 'ITION', 'ITIVE', 'IVELY', 'ULOUS', 'ENCY', 'SION',
             'HOOD', 'NESS', 'IOUS', 'MENT', 'ABLE', 'WARD', 'LESS', 'SELF', 'IBLE', 'SOME',
             'SHIP', 'STER', 'IEST', 'ANCY', 'ICAL', 'ATIC', 'ENCE', 'ANCE', 'IBLY', 'ABLY',
             'ALLY', 'TIVE', 'TION', 'AGE', 'BLE', 'IFY', 'ISH', 'OUS', 'ING', 'UAL', 'FUL',
             'IED', 'ACY', 'ISE', 'IAL', 'ILY', 'YZE', 'IST', 'ANT', 'IES', 'ATE', 'URE', 'ENT',
             'ORY', 'ERY', 'ITE', 'ARY', 'IVE', 'EER', 'ETY', 'ITY', 'IAN', 'IZE', 'ISM', 'LTY',
             'EST', 'IC', 'AL', 'ES', 'ED', 'ND', 'EE', 'LY', 'ER', 'OR', 'TH', 'RD']
                
    codes = ['BY', 'BY', 'RY', 'V', 'FY', 'GY', 'LY', 'N', 'RY', 'TS', 'TZ', 'N', 'V', 'VY', 'X',
             'CY', 'N', 'HD', 'NS', 'X', 'M', 'L', 'WD', 'LS', 'F', 'L', 'SM', 'SP', 'SR', 'ST', 'CY',
             'CL', 'C', 'C', 'C', 'BY', 'BY', 'LY', 'V', 'N', 'J', 'L', 'FY', 'H', 'X', 'G', 'L', 'F',
             'D', 'CY', 'Z', 'L', 'LY', 'Z', 'ST', 'T', 'S', 'T', 'U', 'T', 'RY', 'RY', 'T', 'RY', 'V',
             'R', 'TY', 'TY', 'N', 'Z', 'M', 'LY', 'ST', 'C', 'L', 'S', 'D', 'D', 'E', 'Y', 'R', 'R',
             'H', 'D']
    
    for j in suffs:
        text = text.replace(" {} ".format(j)," {}* ".format(j))
    

    for i,j in zip(codes,suffs):
        text = text.replace(j + " ", i + "* ")



    text = text.replace("*", "")

    return text
    
print("\n")
print(ptext)
print("\n")
ctext = suffixes(ptext)
print(ctext)
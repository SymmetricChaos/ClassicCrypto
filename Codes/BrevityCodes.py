# https://people.duke.edu/~ng46/collections/evans-basic-english-1947.pdf

from PrepareText import preptext3


textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\WindyHill.txt', 'r')
ptext = preptext3(textfile.readline())


def suffixes(text):
    codes = ["BY","C","CL","CY","D","E","F","FY","G","GY",
             "H","HD","J","L","LY","LS","M","N","NS","R",
             "RY","S","SM","SP","SR","ST","T","TS","TY",
             "TZ","U","V","VY","WD","X","Y","Z"]
    suffs = [["ABILITY","IBILITY","ABLY","IBLY"],
             ["ANCE","ENCE","ATIC","IC"],
             ["ICAL"],
             ["ACY","ANCY","ENCY"],
             ["IED","ED","ND","RD"],
             ["EE"],
             ["FUL","SELF"],
             ["FULLY","IFY"],
             ["ING"],
             ["OLOGY"],
             ["ISH","TH"],
             ["HOOD"],
             ["AGE"],
             ["ABLE","IBLE","BLE","IAL","UAL","AL"],
             ["ALLY","ILITY","ILY","LTY"],
             ["LESS"],
             ["ISM","MENT"],
             ["ATION","ITION","TION","SION","IAN"]]
    
    for j in suffs:
        for x in j:
            text = text.replace(" {} ".format(x)," {}* ".format(x))
    
    for i,j in zip(codes,suffs):
        for x in j:
            text = text.replace(x + " ", i + "* ")

    text = text.replace("*", "")

    return text
    
print("\n")
print(ptext)
print("\n")
ctext = suffixes(ptext)
print(ctext)
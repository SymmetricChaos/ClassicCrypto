# https://people.duke.edu/~ng46/collections/evans-basic-english-1947.pdf

from PrepareText import preptext3


textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\WindyHill.txt', 'r')
ptext = preptext3(textfile.readline())

def suffixes(text):
    codes = ["BY","C","CL","CY","D","E","F","FY","G"]
    suffs = [["ABILITY","IBILITY","ABLY","IBLY"],
             ["ANCE","ENCE","ATIC","IC"],
             ["ICAL"],
             ["ACY","ANCY","ENCY"],
             ["IED","ED","ND","RD"],
             ["EE"],
             ["FUL","SELF"],
             ["FULLY","IFY"],
             ["ING"]]
    for i,j in zip(codes,suffs):
        for x in j:
            text = text.replace(x + " ", i + " ")

    return text
    
print("\n")
print(ptext)
print("\n")
ctext = suffixes(ptext)
print(ctext)
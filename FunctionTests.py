from PrepareText import preptext
from VigenereCipher import vigenere,multiVigenere,vigenereAutokey,affineVigenere
from ColumnarTransport import columnarTransport,doubleColumnarTransport
from CaesarCipher import caesar,affine

textfile = open('text1.txt', 'r')
ptext = preptext(textfile.readline())

ctext = caesar(ptext,1)
dtext = caesar(ctext,1,decode=True)
print("Ceasar decode matches plaintext: {}\n".format(dtext == ptext))

ctext = affine(ptext,2,3)
dtext = affine(ctext,2,3,decode=True)
print("Affine decode matches plaintext: {}\n".format(dtext == ptext))

ctext = vigenere(ptext,"THISISABOUTFARMING")
dtext = vigenere(ctext,"THISISABOUTFARMING",decode=True)
print("Vigenere Cipher decode matches plaintext: {}\n".format(dtext == ptext))

ctext = multiVigenere(ptext,["SUGAR","CANE","HARVEST"])
dtext = multiVigenere(ctext,["SUGAR","CANE","HARVEST"],decode=True)
print("MultiVigenere decode matches plaintext: {}\n".format(dtext == ptext))

ctext = vigenereAutokey(ptext,"FARMING")
dtext = vigenereAutokey(ctext,"FARMING",decode=True)
print("VigenereAutokey decode matches plaintext: {}\n".format(dtext == ptext))

ctext = affineVigenere(ptext,"SUGAR","FARMING")
dtext = affineVigenere(ctext,"SUGAR","FARMING",decode=True)
print("AffineVigenere decode matches plaintext: {}\n".format(dtext == ptext))

ctext = columnarTransport(ptext,[5,3,4,1,2,0])
dtext = columnarTransport(ctext,[5,3,4,1,2,0],decode=True)
print("Single Columnar decode matches plaintext: {}\n".format(dtext[:len(ptext)] == ptext))

ctext = doubleColumnarTransport(ptext,[5,3,4,1,6,2,0],[3,1,6,2,0,4,5])
dtext = doubleColumnarTransport(ctext,[5,3,4,1,6,2,0],[3,1,6,2,0,4,5],decode=True)
print("Double Columnar decode matches plaintext: {}\n".format(dtext[:len(ptext)] == ptext))


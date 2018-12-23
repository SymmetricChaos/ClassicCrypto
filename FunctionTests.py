from PrepareText import preptext1
from VigenereCipher import vigenere,multiVigenere,vigenereAutokey,affineVigenere
from ColumnarTransport import columnarTransport,doubleColumnarTransport
from Monoalphabetic import caesar,affine,substitution
from RailfenceCipher import railfence
from PolybiusSquare import polybiusSquare
from Nihilist import nihilistCipher

def decodetest(T1,T2,fun):
    if T1 == T2:
        print("Success")
    else:
        raise Exception("Decode Error With {}".format(fun.__name__))

textfile = open('text1.txt', 'r')
ptext = preptext1(textfile.readline())


ctext = caesar(ptext,1)
dtext = caesar(ctext,1,decode=True)
decodetest(ptext,dtext,caesar)

ctext = affine(ptext,[2,3])
dtext = affine(ctext,[2,3],decode=True)
decodetest(ptext,dtext,affine)

ctext = substitution(ptext,"IOWNAXYLOPHONE",)
dtext = substitution(ctext,"IOWNAXYLOPHONE",decode=True)
decodetest(ptext,dtext,substitution)
    
ctext = vigenere(ptext,"THISISABOUTFARMING")
dtext = vigenere(ctext,"THISISABOUTFARMING",decode=True)
decodetest(ptext,dtext,vigenere)
    
ctext = multiVigenere(ptext,["SUGAR","CANE","HARVEST"])
dtext = multiVigenere(ctext,["SUGAR","CANE","HARVEST"],decode=True)
decodetest(ptext,dtext,multiVigenere)

ctext = vigenereAutokey(ptext,"FARMING")
dtext = vigenereAutokey(ctext,"FARMING",decode=True)
decodetest(ptext,dtext,vigenereAutokey)

ctext = affineVigenere(ptext,["SUGAR","FARMING"])
dtext = affineVigenere(ctext,["SUGAR","FARMING"],decode=True)
decodetest(ptext,dtext,affineVigenere)

ctext = columnarTransport(ptext,[5,3,4,1,2,0])
dtext = columnarTransport(ctext,[5,3,4,1,2,0],decode=True)
decodetest(ptext,dtext[:len(ptext)],columnarTransport)

ctext = doubleColumnarTransport(ptext,[[5,3,4,1,6,2,0],[3,1,6,2,0,4,5]])
dtext = doubleColumnarTransport(ctext,[[5,3,4,1,6,2,0],[3,1,6,2,0,4,5]],decode=True)
decodetest(ptext,dtext[:len(ptext)],doubleColumnarTransport)

ctext = polybiusSquare(ptext,"35ZEBRAS26")
dtext = polybiusSquare(ctext,"35ZEBRAS26",decode=True)
decodetest(ptext,dtext,polybiusSquare)

ctext = railfence(ptext,8)
dtext = railfence(ctext,8,decode=True)
decodetest(ptext,dtext,railfence)

ctext = nihilistCipher(ptext,["NIHILIST","CIPHER"])
dtext = nihilistCipher(ctext,["NIHILIST","CIPHER"],decode=True)
decodetest(ptext,dtext,nihilistCipher)
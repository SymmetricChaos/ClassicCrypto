from VigenereCipher import vigenere
from PrepareText import preptext

def superposition(s,n):
    out = []
    for i in range(1,n):
        ctr = 0
        tempString1 = s[i:len(s)]
        tempString2 = s[0:(len(s)-i)]
        #print(tempString1[:10])
        #print(tempString2[:10])
        for A,B in zip(tempString1,tempString2):
            if A == B:
               ctr += 1
        out.append(ctr)
    return out

textfile = open('text1.txt', 'r')
ptext = preptext(textfile.readline())

ctext = vigenere(ptext,"APPLE")

L = superposition(ptext,100)
print(L)

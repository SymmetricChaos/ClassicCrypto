def rotorEXP(letter,key,ring,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pos = alpha.index(letter)
    inner = key[(pos+ring-1)%26]
    outer = (alpha.index(inner)-ring+1)%26
    #print(letter)
    #print(alpha[(pos+ring-1)%26])
    #print(inner)
    #print(alpha[outer])
    return alpha[outer]

R1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"


for i in range(1,5):
    print(rotorEXP("A",R1,i))
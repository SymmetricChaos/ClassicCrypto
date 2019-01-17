# http://users.telenet.be/d.rijmenants/en/enigmatech.htm#rotorencryption
# http://enigmaco.de/enigma/enigma.html
    

def ringSetting(key,n):
    for i in range(n-1):
        key = key[1:] + key[0]
    return key

def rotorEXP(letter,key,pos,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    entry = alpha.index(letter)
    
    if decode == False:
        inner = key[(entry+pos-1)%26]
        outer = (alpha.index(inner)-pos+1)%26
        #print(letter,end=" -> ")
        #print(alpha[(entry+pos-1)%26],end=" -> ")
        #print(inner,end=" -> ")
        #print(alpha[outer],end=" -> ")
        return alpha[outer]
    if decode == True:
        inner = alpha[(entry+pos-1)%26]
        outer = (key.index(inner)-pos+1)%26
        #print(letter,end=" -> ")
        #print(alpha[(entry+pos-1)%26],end=" -> ")
        #print(inner,end=" -> ")
        #print(alpha[outer],end=" -> ")
        return alpha[outer]

R1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
R2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
R3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
RF = "YRUHQSLDPXNGOKMIEBFZCWVJAT"


T = rotorEXP("A",R1,1)
print(T)
T = rotorEXP(T,R2,1)
print(T)
T = rotorEXP(T,R3,1)
print(T)
T = rotorEXP(T,RF,1)
print(T)
T = rotorEXP(T,R3,1,True)
print(T)
T = rotorEXP(T,R2,1,True)
print(T)
T = rotorEXP(T,R1,1,True)
print(T)
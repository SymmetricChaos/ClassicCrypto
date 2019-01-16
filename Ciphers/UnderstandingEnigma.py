def rotorEXP(letter,key,pos,ring,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sh = key.index(pos)+1
    print(letter)
    print(alpha[alpha.index(letter)-sh])
    print(key[alpha.index(letter)-sh])


R1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

def ringsetting(letter,setting):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(alpha.index(letter))

    
ringsetting("A","A")
from Attacks.TextScoring import quadgramScore
from Ciphers.Playfair import playfair



textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\Dictionary.csv', 'r')
L = []
for i in textfile.readlines():

    if len(i) > 5:
        L.append(i[:-1])
        
    if i[:-1] == L[-1]:
        continue

def dictionaryAttack(ctext,cipher,silent=False):

    bestScore = quadgramScore(ctext)
    bestKey = "A"
    bestText = ctext
    
    for ctr,keyword in enumerate(L):
        t = cipher(ctext,keyword,decode=True)
        q = quadgramScore(t)

        if ctr % 5000 == 0 and silent == False:
            print("!",end="")
        if q > bestScore:
            bestScore = q
            bestKey = keyword
            bestText = t
            if silent == False:
                print("\n")
                print(t[:100])
                print(keyword)
    
    return bestText, bestKey
        
        

def dictionaryAttackExample():
    ctext = "RBQRFIIVTSNPFRZNDLNPFREMSDVPVDLUVELZTIVTUNMVSDRTPOIVFVRCCZRLPESDZLMFPRULADZB"
    dictionaryAttack(ctext,playfair)
    
#dictionaryAttackExample()
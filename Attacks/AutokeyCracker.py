import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import VigenereCipher as vig
from TextScoring import quadgramScore, bigramScore



def autokeyAttack(ctext,klen):
    k = ["A"]*klen
    bestKey = k[:]
    bestScore = quadgramScore(ctext)

    for i in range(klen):
        for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            tempKey = bestKey[:]
            tempKey[i] = l
            dtext = vig.vigenereAutokey(ctext,tempKey,decode=True)
            score = bigramScore(dtext)
            if score > bestScore:
                bestKey = tempKey
                bestScore = score
    print(bestKey)
    print(vig.vigenereAutokey(ctext,bestKey,decode=True))
    
    
    
ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
ctext = vig.vigenereAutokey(ptext,"MYKEYVALUE")

autokeyAttack(ctext,10)

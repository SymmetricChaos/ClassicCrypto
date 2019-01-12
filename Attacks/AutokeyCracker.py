import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import VigenereCipher as vig
from TextScoring import bigramScore



def autokeyAttack(ctext,limit=30):
    outKey = ["A"]
    outScore = bigramScore(ctext)
    for klen in range(2,limit):
        bestKey = ["A"]*klen
        bestScore = bigramScore(ctext)
    
        for i in range(klen):
            for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                tempKey = bestKey[:]
                tempKey[i] = l
                dtext = vig.vigenereAutokey(ctext,tempKey,decode=True)
                score = bigramScore(dtext)
                if score > bestScore:
                    bestKey = tempKey
                    bestScore = score
        if bestScore > outScore:
            outScore = bestScore
            outKey = bestKey
    print("Best Key Found:")
    print("".join(outKey))
    print()
    print(vig.vigenereAutokey(ctext,outKey,decode=True))
    print()
        
    
    
ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
ctext = vig.vigenereAutokey(ptext,"ALONGBITOFGIBBERISH")

autokeyAttack(ctext)

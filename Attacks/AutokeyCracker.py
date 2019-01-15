import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import VigenereCipher as vig
from TextScoring import bigramScore


# This attack on the autokey cipher is surprisngly simple. Since we have no way
# of determining the length of the key we will have to test many different
# key lengths. By default we check every key length from 2 to 30.

# To find the best key we first assume it is the letter A repeated many times
# which represents no key at all. Then we change the first letter of the key
# and test if it looks better. After going through all 26 posibilities for the
# first letter we do the same for the second. Then the third and so on.

def autokeyAttack(ctext,limit=20):
    # Our starting score
    outKey = ["A"]
    outScore = bigramScore(ctext)
    
    # Try every key length
    for klen in range(2,limit):
        
        # Start with the simplest key and its score
        bestKey = ["A"]*klen
        bestScore = bigramScore(ctext)
    
        # For each position
        for i in range(klen):
            # Try every possible letter in that position
            for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                tempKey = bestKey[:]
                tempKey[i] = l
                dtext = vig.vigenereAutokey(ctext,tempKey,decode=True)
                score = bigramScore(dtext)
                # If this is the best so far save it
                if score > bestScore:
                    bestKey = tempKey
                    bestScore = score
        
        # If this key length produced a better decode than any previous key
        # length we make it the one we will save.
        if bestScore > outScore:
            outScore = bestScore
            outKey = bestKey
    
    print("Best Key Found:")
    print("".join(outKey))
    print()
    print(vig.vigenereAutokey(ctext,outKey,decode=True))
    print()
        
    
    
ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
ctext = vig.vigenereAutokey(ptext,"BILBBREGZO")

autokeyAttack(ctext)

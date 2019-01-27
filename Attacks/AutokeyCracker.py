import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.Autokey import autokey
from TextScoring import bigramScore


# This attack on the autokey cipher is surprisngly simple. Since we have no way
# of determining the length of the key we will have to test many different
# key lengths. By default we check every key length from 2 to 30.

# To find the best key we first assume it is the letter A repeated many times
# which represents no key at all. Then we change the first letter of the key
# and test if it looks better. After going through all 26 posibilities for the
# first letter we do the same for the second. Then the third and so on.

def autokeyCracker(ctext,limit=20):
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
                dtext = autokey(ctext,tempKey,decode=True)
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
    print(autokey(ctext,outKey,decode=True))
    print()
        
def autokeyCrackerExample():
    
    print("""
Example of an Attack on the Autokey Cipher

Because there is no cyclic pattern to the key for us to exploit we have no way
to determine what the length of the key is we will have to try many possible
key lengths. By default keys with a length up to 20 are tried.
""")
    
    ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
    ctext = autokey(ptext,"BILBBREGZO")
    
    print(ctext,"\n\n")
    autokeyCracker(ctext)

autokeyCrackerExample()
# Testing if the simple Hill Climbing method will work on the Playfair cipher

import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import Playfair as pf
from TextScoring import quadgramScore
import random



def hillclimbing(ctext):
    
    # Setup
    finalScore = float("-infinity")
    finalKey = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
    # There will be one thousand rounds of attempts to break the cipher
    # The reason we have multiple rounds is because we might get stuck in a 
    # local minima while mutating the results.
    # Occasionally resetting gives coverage of more of the possible search
    # space.
    for x in range(2000):
        # To start the round we randomize the alphabet to start with
        key = [i for i in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
        random.shuffle(key)
        
        # Our starting score is whatever we got from this
        out = pf.playfairCipher(ctext,"".join(key),decode=True)
        bestscore = quadgramScore(out)
        bestkey = "".join(key)
     
        # Within each round we keep mutating the key until we go a few thousand
        # mutations without improvement.
        ctr = 0
        while ctr < 1000:
            # Count how many mutations since the last improvement
            ctr += 1
            
            # A copy of the key list that we can mutate
            newKey = key[:]
            
            # The mutation is swapping two letters
            A = random.randint(0,24)
            B = random.randint(0,24)
            newKey[A],newKey[B] = newKey[B],newKey[A]
            
            # Try it and see what score we get
            out = pf.playfairCipher(ctext,"".join(newKey),decode=True)
            score = quadgramScore(out)
            
            # If that score is better than before write it down and reset the
            # counter.
            if score > bestscore:
    
                ctr = 0
                key = newKey
                bestkey = newKey
                bestscore = score
    
        # At the end of each round check if it produced a better score than
        # any previous round. If it did then write it down and print some
        # information.
        if bestscore > finalScore:
            finalKey = bestkey
            finalScore = bestscore
            print("\n\nRound {}".format(x))
            print("Key Looks Like:")
            #print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            print("".join(finalKey))
            print()
            print(pf.playfairCipher(ctext,"".join(finalKey),decode=True))
            print("\n")
        else:
            print("#",end="")
            if (x + 1) % 45 == 0:
                print()


ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
ctext = pf.playfairCipher(ptext,"PLAYFAIR")
hillclimbing(ctext)
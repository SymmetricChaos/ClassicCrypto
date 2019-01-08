# Testing if the simple Hill Climbing method will work on the Playfair cipher

import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import Playfair as pf
from TextScoring import quadgramScore
import random
import math


def simulatedAnnealing(ctext):
        
    
    # There will be one thousand rounds of attempts to break the cipher
    # The reason we have multiple rounds is because we might get stuck in a 
    # local minima while mutating the results.
    # Occasionally resetting gives coverage of more of the possible search
    # space.
    for x in range(20):
        # To start the round we randomize the alphabet to start with
        key = [i for i in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
        random.shuffle(key)
        
        # Our starting score is whatever we got from this
        out = pf.playfairCipher(ctext,"".join(key),decode=True)
        bestscore = quadgramScore(out)
        bestkey = "".join(key)
     
        # Within each round we 
        for temp in range(10,0,-1):
            print(temp,end=" ")
            for i in range(40000):

                # A copy of the key list that we can mutate
                newKey = key[:]
            
                # The mutation is swapping two letters
                A = random.randint(0,24)
                B = random.randint(0,24)
                newKey[A],newKey[B] = newKey[B],newKey[A]
                
                # Try it and see what score we get
                out = pf.playfairCipher(ctext,newKey,decode=True,mode="FAST")
                score = quadgramScore(out)

                
                # If that score is better we always take the new key
                # If it is worse then there is a chance we will accept it
                # anyway. When the temperature is high, early in the process,
                # it is more likely we will pick a worse score.
                if score > bestscore:
                    key = newKey
                    bestkey = newKey
                    bestscore = score
                else:
                    scorediff = (score - bestscore)/1000

                    pr = math.exp(scorediff/temp)

                    if random.uniform(0,1) > pr:
                        key = newKey
                        bestkey = newKey
                        bestscore = score
    


        print("\n\nRound {}".format(x))
        print("Key Looks Like:")
        print("".join(bestkey))
        print()
        print(pf.playfairCipher(ctext,"".join(bestkey),decode=True))
        print("\n")



ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
ctext = pf.playfairCipher(ptext,"PLAYFAIR")
simulatedAnnealing(ctext)
# Testing if the simple Hill Climbing method will work on the Playfair cipher

import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import Playfair as pf
from TextScoring import quadgramScore
import random
import math
import numpy as np

def swapLetters(key):
    A,B = random.sample([i for i in range(25)],2)
    key[A],key[B] = key[B],key[A]
    
def swapRows(key):
    A,B = random.sample([0,1,2,3,4],2)
    key[5*A:5*A+5],key[5*B:5*B+5] = key[5*B:5*B+5],key[5*A:5*A+5]

def swapCols(key):
    A,B = random.sample([0,1,2,3,4],2)
    for i in range(5):
        t = key[i*5 + A]
        key[i*5 + A] = key[i*5 + B]
        key[i*5 + B] = t

def rotate(key):
    A = random.randint(1,23)
    for i in range(A):
        key.append(key.pop(0))

def simulatedAnnealing(ctext):

    # There will be one thousand rounds of attempts to break the cipher
    # The reason we have multiple rounds is because we might get stuck in a 
    # local minima while mutating the results.
    # Occasionally resetting gives coverage of more of the possible search
    # space.
    for x in range(50):
        # To start the round we randomize the alphabet to start with
        key = [i for i in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
        random.shuffle(key)
        
        # Our starting score is whatever we got from this
        out = pf.playfairCipher(ctext,"".join(key),decode=True)
        bestscore = quadgramScore(out)
        bestkey = "".join(key)
     
        # The "temperature" decreases gradually with each round. The higher the
        # temperature the more likely the algorithm is to accept a change.
        for temp in np.linspace(20,.2,100):
            print("!",end="")
            for i in range(20000):

                # A copy of the key list that we can mutate
                newKey = key[:]
            
                # Choose which kind of mutation to apply
                mutType = random.randint(0,99)
                if mutType < 80:
                    swapLetters(newKey)
                if mutType >= 80 and mutType < 85:
                    swapRows(newKey)
                if mutType >= 85 and mutType < 90:
                    swapCols(newKey)
                if mutType >= 90 and mutType < 95:
                    rotate(newKey)
                if mutType >= 95:
                    newKey.reverse()
    
                
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
    


        print("\n\nRound {}".format(x+1))
        print("Best Key Found:")
        print("".join(bestkey))
        print()
        print(pf.playfairCipher(ctext,"".join(bestkey),decode=True))
        print("\n")


ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
ctext = pf.playfairCipher(ptext,"PLAYFAIR")
#ctext = "XZOGQRWVQWNROKCOAELBXZWGEQYLGDRZXYZRQAEKLRHDUMNUXYXSXYEMXEHDGNXZYNTZONYELBEUGYSCOREUSWTZRLRYBYCOLZYLEMWNSXFBUSDBORBZCYLQEDMHQRWVQWAEDPGDPOYHORXZINNYWPXZGROKCOLCCOCYTZUEUIICERLEVHMVQWLNWPRYXHGNMLEKLRHDUYSUCYRAWPUYECRYRYXHGNBLUYSCCOUYOHRYUMNUXYXSXYEMXEHDGN"
simulatedAnnealing(ctext)
import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import Monoalphabetic as sub
from TextScoring import quadgramScore
import random



def hillclimbing(ctext):
    
    # Setup
    finalScore = float("-infinity")
    finalKey = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
    # There will be one thousand rounds of attempts to break the cipher
    for x in range(1000):
        # To start the round we randomize the alphabet to start with
        key = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        random.shuffle(key)
        
        # Our starting score is whatever we got from this
        out = sub.substitution(ctext,"".join(key),decode=True)
        bestscore = quadgramScore(out)
        bestkey = "".join(key)
     
        # Within each round we keep mutating the key until we go a few thousand
        # mutations without improvement.
        ctr = 0
        while ctr < 2000:
            # Count how many mutations since the last improvement
            ctr += 1
            
            # A copy of the key list that we can mutate
            newKey = key[:]
            
            # The mutation is swapping two letters
            A = random.randint(0,25)
            B = random.randint(0,25)
            newKey[A],newKey[B] = newKey[B],newKey[A]
            
            # Try it and see what score we get
            out = sub.substitution(ctext,"".join(newKey),decode=True)
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
            
            print("Round {}".format(x))
            print("Key Looks Like:")
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            print("".join(finalKey))
            print()
            print(sub.substitution(ctext,"".join(finalKey),decode=True))
            print("\n")

        
        
    
ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
ctext = sub.substitution(ptext,key="SIMPLESUBTITUTION")

ctext = "SOWFBRKAWFCZFSBSCSBQITBKOWLBFXTBKOWLSOXSOXFZWWIBICFWUQLRXINOCIJLWJFQUNWXLFBSZXFBTXAANTQIFBFSFQUFCZFSBSCSBIMWHWLNKAXBISWGSTOXLXTSWLUQLXJBUUWLWISTBKOWLSWGSTOXLXTSWLBSJBUUWLFULQRTXWFXLTBKOWLBISOXSSOWTBKOWLXAKOXZWSBFIQSFBRKANSOWXAKOXZWSFOBUSWJBSBFTQRKAWSWANECRZAWJ"
ctext = ctext.upper()

hillclimbing(ctext)
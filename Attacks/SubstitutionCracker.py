# based on http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-simple-substitution-cipher/

from Ciphers.Substitution import substitution
from TextScoring import quadgramScore
import random



def hillclimbing(ctext,rounds=1000):
    
    # Setup
    finalScore = float("-infinity")
    finalKey = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
    # There will be one thousand rounds of attempts to break the cipher
    # The reason we have multiple rounds is because we might get stuck in a 
    # local minima while mutating the results.
    # Occasionally resetting gives coverage of more of the possible search
    # space.
    for x in range(rounds):
        # To start the round we randomize the alphabet to start with
        key = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        random.shuffle(key)
        
        # Our starting score is whatever we got from this
        out = substitution(ctext,"".join(key),decode=True)
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
            out = substitution(ctext,"".join(newKey),decode=True)
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
        if bestscore >= finalScore:
            finalKey = bestkey
            finalScore = bestscore
            print("\n\nRound {}".format(x))
            print("Key Looks Like:")
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            print("".join(finalKey))
            print()
            print(substitution(ctext,"".join(finalKey),decode=True))
            print("\n")
        else:
            print("#",end="")



ctext = "SOWFBRKAWFCZFSBSCSBQITBKOWLBFXTBKOWLSOXSOXFZWWIBICFWUQLRXINOCIJLWJFQUNWXLFBSZXFBTXAANTQIFBFSFQUFCZFSBSCSBIMWHWLNKAXBISWGSTOXLXTSWLUQLXJBUUWLWISTBKOWLSWGSTOXLXTSWLBSJBUUWLFULQRTXWFXLTBKOWLBISOXSSOWTBKOWLXAKOXZWSBFIQSFBRKANSOWXAKOXZWSFOBUSWJBSBFTQRKAWSWANECRZAWJ"
#ctext = "JCWDAMJSBYAOFBVICFVCAKUGJKJVJKRFKVKCFTXJPSPAIKJIFBGOPVCWDANAGJADAOJVJMJOOJOPVCWDAUYFFMIJVCWCAWDGCAWYVJJPMOYRGFBVCWVJKRGSFFOMYJAPOKVWPGAGGADJKFPJCFUAGFBTWPVWXAOBAWTVJFPNAMFYAJVJKVFFGWVA"
#ctext = "ABCDEFBEDBCEAGHICDJKLCKKJMNBL"
hillclimbing(ctext,rounds=5000)
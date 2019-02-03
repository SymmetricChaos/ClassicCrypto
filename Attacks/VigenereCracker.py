from Ciphers.Vigenere import vigenere
from Ciphers.UtilityFunctions import preptext, factors
from FrequencyAnalysis import frequencyTable
from TextScoring import bigramScore


# While a Vigenere cipher does effectively resist traditional frequency
# analysis a critical weakness is that is it made up of several very weak
# Caesar ciphers. If the key length is known then each of those ciphers can be
# broken individually with little effort.

# Kasiski examination is a way of estimating the length of they key when only
# the ciphertext is known. Because the key is repeated and because certain
# letter sequences are common in language it will happen that they line up
# occasionally. The distance between these repetitions will be some multiple of
# the key length.

# This attack on the Vigenere cipher works by finding these repetitions and
# then factoring the distances between them to make a list of possible key
# lengths. Then each of these possible key lengths is attacked and the output
# checked for how well it matches English text. The best of these results is
# returned.


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1
        
def diffs(L):
    for i in range(len(L)-1):
        yield L[i+1]-L[i]

def vigenereKeyLength(s):
    
    # Find the ten most common 4-grams
    sizes = []
    for i in frequencyTable(ctext,4)[:10]:
        L = []
        # Find the position of each of them
        for j in find_all(ctext,i[0]):
            L.append(j)
    
        # Check the distance between each of them 4-grams
        # Then factor the distances to find the likely key lengths
        for d in diffs(L):
            for s in factors(d):
                sizes.append(s)
                
    return frequencyTable(sizes)

def solveVigenere(s,klen=0,verbose=True):
    
    if klen == 0:
    
        ftable = vigenereKeyLength(s)
        keylens = [i[0] for i in ftable]
        
        ## Knowing that the Vigenere cipher is made of many Caesar ciphers we
        ## can simply check for the most common letter and shift to make it appear
        ## as the letter E
        bestscore = float("-inf")
        finalKEY = ""
        finalDECODE = "" 
        for k in keylens:
            slices = [[] for i in range(k)]
            
            for i,let in enumerate(s):
                slices[i%k].append(let)
                
            x = []
            for i in slices:
                # Most common letter
                c = frequencyTable(i)[0][0]
                x.append( chr((ord(c)-69)%26+65) )
                
            KEY = "".join(x)
            dtext = vigenere(ctext,KEY,decode=True)
            score = bigramScore(dtext)
            if score > bestscore:
                bestscore = score
                finalKEY = KEY
                finalDECODE = dtext
                
        if verbose == True:
            print("They key length is probably: {}".format(len(finalKEY)))
            print("Based on that the key should be: {}".format(finalKEY))
            print("The text begins:\n{}".format(finalDECODE[:70]))
            print("This translation scores: {0:0.0f}".format(bestscore))
    
        return finalDECODE,finalKEY,bestscore
    
    else:
        slices = [[] for i in range(klen)]
            
        for i,let in enumerate(s):
            slices[i%klen].append(let)
                
        x = []
        for i in slices:
            # Most common letter
            c = frequencyTable(i)[0][0]
            x.append( chr((ord(c)-69)%26+65) )
                
        KEY = "".join(x)
        dtext = vigenere(ctext,KEY,decode=True)
        score = bigramScore(dtext)

        if verbose == True:
            print("Assuming a key length of: {}".format(klen))
            print("Based on that the key should be: {}".format(KEY))
            print("The text begins:\n{}".format(dtext[:70]))
            print("This translation scores: {0:0.0f}".format(score))
    


textfile = open('text1.txt', 'r')
ptext = preptext(textfile.readline(),silent=True)
ctext = vigenere(ptext,"ZEBRAS")

solveVigenere(ctext)


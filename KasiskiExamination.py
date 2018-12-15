# Reference thesse sites for some improvements
# https://www.guballa.de/vigenere-solver
# https://en.wikipedia.org/wiki/Kasiski_examination

from VigenereCipher import vigenere
from PrepareText import preptext1
from FrequencyAnalysis import frequencyTable
from MathFunctions import factors

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

def bigramScoring(text):
    ngrams2 = open('2grams.csv', 'r')
    bigrams = {}
    for n,line in enumerate(ngrams2):
        L = line.split(",")
        bigrams[L[0]] = 676-n
    score = 0
    for i in range(len(text)-1):
        score += bigrams[text[i:i+2]]
    return score

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

def solveVigenere(s,verbose=True):
    ftable = vigenereKeyLength(s)
    keylens = [i[0] for i in ftable]
    
    ## Knowing that the Vigenere cipher is made of many Caesar ciphers we
    ## can simply check for the most common letter and shift to make it appear
    ## as the letter E
    bestscore = 0
    finalKEY = ""
    finalDECODE = "" 
    for k in keylens:
        slices = [[] for i in range(k)]
        
        for i,let in enumerate(s):
            slices[i%k].append(let)
            
        k = []
        for i in slices:
            # Most common letter
            c = frequencyTable(i)[0][0]
            k.append( chr((ord(c)-69)%26+65) )
        KEY = "".join(k)
        dtext = vigenere(ctext,KEY,decode=True)
        score = bigramScoring(dtext)
        if score > bestscore:
            bestscore = score
            finalKEY = KEY
            finalDECODE = dtext

    if verbose == True:
        print("They key length is probably: {}".format(len(finalKEY)))
        print("Based on that the key should be: {}".format(finalKEY))
        print("The text begins:\n{}".format(finalDECODE[:70]))
        print("This translation scores: {}".format(bestscore))

    return finalDECODE,finalKEY,bestscore


textfile = open('text1.txt', 'r')
ptext = preptext1(textfile.readline())
ctext = vigenere(ptext,"ZEBRASPIZZA")

solveVigenere(ctext)


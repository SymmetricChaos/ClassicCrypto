from itertools import permutations
from TextScoring import bigramScore
from ColumnarTransport import columnarTransport
from MathFunctions import factors
from PrepareText import preptext1

def columnarBruteForce(text,lim=8):
    F = factors(len(text))
    print("Testing key lengths of: {}".format([i for i in F if i < lim]))
    L = []
    for i in F:
        if i <= lim:
            bestdtext = ""
            bestscore = float("-inf")
            for p in permutations([x for x in range(i)]):
                dtext = columnarTransport(text,p,True)
                score = bigramScore(dtext)
                if score > bestscore:
                    bestscore = score
                    bestdtext = dtext
            L.append(bestdtext)
    return L
            
textfile = open('text1.txt', 'r')
ptext = preptext1(textfile.readline())
ctext = columnarTransport(ptext,[4,0,1,3,2,5])
D = columnarBruteForce(ctext)
print("Candidate Decrypts")
for i in D:
    print(i[:60])

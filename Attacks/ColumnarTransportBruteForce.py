import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.ColumnarTransport import columnarTransport
from TextScoring import quadgramScore
from itertools import permutations
from UtilityFunctions import factors
from PrepareText import preptext1

def columnarBruteForce(text):
    
    # We could try every possible key up to some limit but we can easily rule
    # out the majority of such keys. Because of how the columnar transport
    # cipher works the key length must be a factor of the length of the
    # ciphertext. We can forcibly stop when we find a good candidate.
    
    
    F = factors(len(text))
    print("Testing key lengths of: {}".format([i for i in F]))
    for i in F:
        bestdtext = ""
        bestscore = float("-inf")
        for p in permutations([x for x in range(i)]):
            dtext = columnarTransport(text,p,True)
            score = quadgramScore(dtext)
            if score > bestscore:
                bestscore = score
                bestdtext = dtext
        print("\nBest Decrypt For Key Length {}".format(i))
        print(bestdtext[:100])




textfile = open('text1.txt', 'r')
ptext = preptext1(textfile.readline())
ctext = columnarTransport(ptext,[4,0,1,3,2,5])
columnarBruteForce(ctext)


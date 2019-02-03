from Ciphers.ColumnarTransport import columnarTransport
from Ciphers.UtilityFunctions import factors, preptext
from TextScoring import quadgramScore
from itertools import permutations

def columnarTransportCracker(text):
    
    # We could try every possible key up to some limit but we can easily rule
    # out the majority of such keys. Because of how the columnar transport
    # cipher works the key length must be a factor of the length of the
    # ciphertext. We can forcibly stop when we find a good candidate.
    
    
    F = factors(len(text))
    print("Testing key lengths of: {}".format([i for i in F]))
    for i in F:
        bestdtext = ""
        bestscore = float("-inf")
        bestkey = []
        for p in permutations([x for x in range(i)]):
            dtext = columnarTransport(text,p,True)
            score = quadgramScore(dtext)
            if score > bestscore:
                bestscore = score
                bestdtext = dtext
                bestkey = p
        print("\nBest Decrypt For Key Length {}".format(i))
        print("Best Key Looks Like: {}".format(bestkey))
        print(bestdtext[:100])


def columnarTransportCrackerExample():

    print("""
For single columnar transport the length of the key must be a factor of the
length of the ciphertext. This brute force attack first calculates those
factors then tries every possible key for each of those lengths. This is not
practical if the length of the key is more than about nine.
""")
    
    textfile = open('text1.txt', 'r')
    ptext = preptext(textfile.readline(),silent=False)
    ctext = columnarTransport(ptext,"MYSTIC")
    columnarTransportCracker(ctext)

#columnarTransportCrackerExample()
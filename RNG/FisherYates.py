def fisherYatesShuff(K,rand):
    if K > len(rand):
        raise Exception("Not enough random numbers.")
    
    L = [i for i in range(K)]
    
    out = []
    
    for i in range(1,K):

        r = rand[i]

        out.append(L.pop( r % (K-i) ))

    return out

def fisherYatesShuffExample():
    from RNG.LCG import LCG
    from itertools import islice, product
    
    suits = ["\u2663", "\u2665", "\u2660", "\u2666"]
    ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = []
    for i in product(ranks,suits):
        deck.append("".join(i))

    R = [i for i in islice(LCG(1000,151,73,43),52)]
    #print(R)
    #print("\n")
    shuf = fisherYatesShuff(52,R)
    #print(shuf)

    print([deck[i] for i in shuf])

fisherYatesShuffExample() 
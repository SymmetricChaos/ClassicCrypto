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
    for i,j in product(suits,ranks):
        deck.append("".join([j,i]))

    print("Deck of Cards in Standard Order")
    print(deck)

    R = [i for i in islice(LCG(555,1000,73,123),52)]
    print("\nPseudo-Random Numbers")
    print(R)
    
    shuf = fisherYatesShuff(52,R)
    print("\nFisher-Yates Positions")    
    print(shuf)

    print("\nShuffled Deck")
    print([deck[i] for i in shuf])

#fisherYatesShuffExample()
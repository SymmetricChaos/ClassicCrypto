from RNG.LCG import LCG
from itertools import islice

def fisherYatesShuff(K,rand):
    if K > len(rand):
        raise Exception("Not enough random numbers.")
    
    L = [i for i in range(K)]
    
    out = []
    
    for i in range(1,K):

        r = rand[i]

        out.append(L.pop( r % (K-i) ))

    return out
    
R = [i for i in islice(LCG(1000,151,73,43),52)]
print(R)
print("\n")
print( fisherYatesShuff(52,R) )
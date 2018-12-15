import string
from MathFunctions import primes


def godelencoding(S,decode=False):
    
    if decode == False:
        alpha = string.ascii_uppercase
        D = {x:ord(x)-64 for x in alpha}
        
        out = 1
            
        for let,pr in zip(S,primes()):
            out *= pr**D[let]
                
        return out

def godelcode(S,decode=False):
    if decode == False:
        T = S.split(" ")
        L = []
        for i in T:
            L.append(str(godelencoding(i)))
        return "|".join(L)

    if decode == True:
        out = []
        N = S.split("|")
        for n in N:
            t = int(n)
            for p in primes():
                ctr = 0
                while t % p == 0:
                   ctr += 1
                   t = t // p
                out.append(chr(ctr+64))
                if t == 1:
                    break
            out.append(" ")
        return "".join(out)
    

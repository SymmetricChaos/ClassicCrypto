import string

def primes():
    D = {}
    q = 2
    while True:
        if q not in D:

            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def godelencoding(S):
    alpha = string.ascii_uppercase
    D = {x:ord(x)-64 for x in alpha}

    out = 1
    
    for let,pr in zip(S,primes()):
        out *= pr**D[let]
        
    print(out)
    return out

for i in ["THIS","FORM","OF","ENCODING","IS","DUE","TO","GODEL","BUT","IS","OBVIOUSLY","MUCH","TOO","INEFFICIENT","TO","USE","IN","THE","WAY","THAT","I","AM","USING","IT","BUT","I","HOPE","YOU","HAD","FUN","WITH","THE","PUZZLE","ANYWAY"]:
    godelencoding(i)
    print()
from Ciphers.UtilityFunctions import uniqueRank


def chainAddition(L,n):
    for i in range(n):
        L.append( (L[i] + L[i+1]) % 10 )

    
def addLists(A,B):
    return [(a+b) % 10 for a,b in zip(A,B)]

def subLists(A,B):
    return [(a-b) % 10 for a,b in zip(A,B)]

def VICkeystream(keys):
    
    # Agent identifier
    aInd = [ int(i) for i in keys[0] ]
    # Random number
    rInd = [ int(i) for i in keys[1] ]
    # Keyphrase
    S = keys[2]
    
    a = subLists(aInd,rInd)
    chainAddition(a,5)
    
    if len(S) != 20:
        raise Exception("Keyphrase must be exactly 20 letters")
    
    n1 = uniqueRank(S[:10])
    n2 = uniqueRank(S[10:])
    
    n1 = [(i+1) % 10 for i in n1]
    n2 = [(i+1) % 10 for i in n2]
    
    addLists(n1,a)
    
    
    print(a)
    print(n1)
    #print(n2)
    print(addLists(n1,a))

    
    #chainAddition(n1[:5],5)

def VIC(text,keys,decode=False):
    if len(text) > 50:
        raise Exception("Text is too long.")
    
    
VICkeystream(["77651","74177","IDREAMOFJEANNIEWITHT"])
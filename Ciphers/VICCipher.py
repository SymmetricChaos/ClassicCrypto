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
    
    # Start the key stream
    kstr = subLists(aInd,rInd)
    chainAddition(kstr,5)
    
    # Use uniqueRank to turn the keyphrase into two lists of 10 numbers
    n1 = uniqueRank(S[:10])
    n2 = uniqueRank(S[10:])
    
    # The historical VIC used a slightly different scheme with 1 for the first 
    # symbol and 0 for the last
    n1 = [(i+1) % 10 for i in n1]
    n2 = [(i+1) % 10 for i in n2]
    
    # Add the first list of numbers to the keystream
    #print(n1)
    #print(kstr)
    kstr = addLists(n1,kstr)

    # Used the second list of numbers to encode the keystream
    #print(nums)
    #print(n2)
    #print(kstr)
    nums = [1,2,3,4,5,6,7,8,9,0]
    kstr = [n2[nums.index(i)] for i in kstr]
    
    #chainAddition(n1[:5],5)

def VIC(text,keys,decode=False):
    if len(text) > 50:
        raise Exception("Text is too long.")
    if len(keys[2]) != 20:
        raise Exception("Keyphrase must be exactly 20 letters")
    
    
VICkeystream(["77651","74177","IDREAMOFJEANNIEWITHT"])
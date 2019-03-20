from Ciphers.UtilityFunctions import uniqueRank, find_all, printColumns, groups
from Ciphers import straddlingCheckerboard
from Ciphers.Transposition import columnarTransport

# The VIC cipher (apparently) treated 0 as greater than 9 in ordering
def VICRank(S):
    L = uniqueRank(S)
    return [ (i+1) % 10 for i in L]
    
# Quickly apply the chain addition, fibonnaci 
def chainAddition(L,n):
    for i in range(n):
        L.append( (L[i] + L[i+1]) % 10 )

    
def addLists(A,B):
    return [(a+b) % 10 for a,b in zip(A,B)]

def subLists(A,B):
    return [(a-b) % 10 for a,b in zip(A,B)]

# Use a list of numbers to shuffle a straddlingCheckerboard with the specific 
# layout used for a VIC style checkerboard
def VICboard(L):
    keys = ["",[]]
    board = ["ET AONR IS","BCDFGHJKLM","PQ/UVWXYZ."]
    for i in range(3):
        board[i] = columnarTransport(board[i],L)
        
    keys[1] = [i for i in find_all(board[0]," ")]
    keys[0] = board[0].replace(" ","") + board[1] + board[2]
    
    return keys

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
    
    # Use VICRank to turn the keyphrase into two lists of 10 numbers
    n1 = VICRank(S[:10])
    n2 = VICRank(S[10:])
    print(n1)
    print(n2)
        
    # Add the first list of numbers to the keystream
    #print(n1)
    #print(kstr)
    kstr = addLists(n1,kstr)

    # Used the second list of numbers to encode the keystream
    nums = [1,2,3,4,5,6,7,8,9,0]
    kstr = [n2[nums.index(i)] for i in kstr]
    #print(nums)
    #print(n2)
    #print(kstr)
    
    chainAddition(kstr,50)
    #print(kstr)
    return kstr



def VIC(text,keys,decode=False):

    if len(keys[2]) != 20:
        raise Exception("Keyphrase must be exactly 20 letters")
        
    kstr = VICkeystream(keys)
    printColumns(kstr[10:],10)
    
    transKey = [ (i-2) % 10 for i in VICRank(kstr[:10])]
    print(kstr[:10])
    print(transKey)
    G = groups(kstr[10:],10)
    print(G)
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ./"

    K = VICboard(kstr[50:])
    print(K)

    print(straddlingCheckerboard(text,keys=K,alphabet=alphabet))
    

VIC("THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG",["77651","74177","IDREAMOFJEANNIEWITHT",8])
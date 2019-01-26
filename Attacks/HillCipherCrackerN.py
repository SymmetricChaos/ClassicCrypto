import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.HillCipher import hillCipher
from Ciphers.UtilityFunctions import groups
from sympy import Matrix, pprint
from Ciphers.PrepareText import preptext1
from Attacks.TextScoring import quadgramScore

def hillCipherAttack(ctext,crib,N):
    
    if len(crib) < N*N:
        raise Exception("crib must have length {}".format(N*N))
    
    bestScore = quadgramScore(ctext)
    bestKey = Matrix.eye(N)
    
    # We can use this to reduce a matrix modulo 26
    mod26 = lambda x : x % 26
    
    # Convert the text and crib to numbers so they're more useful
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ctextN = [alpha.index(i) for i in ctext]
    cribN = [alpha.index(i) for i in crib]
    
    # Break text into pieces
    G = groups(ctextN,N)
    
    for pos in range(len(crib)-(N*N-1)):
        
        subCrib = cribN[pos:pos+(N*N)]
        
        #print(subCrib)
        
        
        A = Matrix(groups(subCrib,N)).T
        
        
        for i in range(len(G)-(N-1)):

            L = []
            for x in range(N):
                L.append(G[x+i])
                B = Matrix(L).T
            
            
            #pprint(B)
            
            # If the matrix is not invertible skip it
            if B.det() % 2 == 0:
                continue
            
            if B.det() % 13 == 0:
                continue
            
            
            C = A*(B.inv_mod(26))
            
            tKey = C.applyfunc(mod26)
        
            # We run the Hill Cipher in encryption mode NOT decryption
            t = hillCipher(ctext,tKey)
            score = quadgramScore(t)
            
            if score > bestScore:
                bestScore = score
                bestKey = tKey
                #print(t[:40])
                
                
    
    #pprint(bestKey.inv_mod(26))
    print(hillCipher(ctext,bestKey))


# Load up the text to use
textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\text1.txt', 'r')
ptext = preptext1(textfile.readline(),silent=True)
ptext = ptext[:201]
print(ptext,"\n\n")
ctext = hillCipher(ptext,[[23,20],[1,21]])
ctext = hillCipher(ptext,[[0,17,5],[1,14,0],[5,20,13]])

crib = "ANDWHEREIT"

dtext = hillCipherAttack(ctext,crib,3)
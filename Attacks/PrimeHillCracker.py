import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.PrimeHillCipher import primeHillCipher, createMatrixKey37
from Ciphers.UtilityFunctions import groups
from sympy import Matrix, pprint
from Ciphers.PrepareText import preptext1
from Attacks.TextScoring import quadgramScore

def primeHillCipherAttack(ctext,crib,N):
    
    if len(crib) < N*N:
        raise Exception("crib must have length {}".format(N*N))
    
    bestScore = quadgramScore(ctext)
    bestKey = Matrix.eye(N)
    
    # We can use this to reduce a matrix modulo 26
    mod37 = lambda x : x % 37
    
    # Convert the text and crib to numbers so they're more useful
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#"
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
            if B.det() % 37 == 0:
                continue
            
            
            C = A*(B.inv_mod(37))
            
            tKey = C.applyfunc(mod37)
        
            # We run the Hill Cipher in encryption mode NOT decryption
            t = primeHillCipher(ctext,tKey)
            score = quadgramScore(t)
            
            if score > bestScore:
                bestScore = score
                bestKey = tKey
                #print(t[:40])
                
    if bestKey.det() % 37 == 0:
        print("Something Strange Happened")
        print("Key Should be Inverse of:")
        pprint(bestKey)
        print()
    else:
        print("Key Is:")
        pprint(bestKey.inv_mod(37))
        print()
    
    print("Decrypt Looks Like:")
    print(primeHillCipher(ctext,bestKey))



# Load up the text to use
textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\text1.txt', 'r')
ptext = preptext1(textfile.readline(),silent=True)
ptext = ptext[:201]
print(ptext,"\n\n")
key = createMatrixKey37(3)
ctext = primeHillCipher(ptext,key)

crib = "INTRODUCED"

dtext = primeHillCipherAttack(ctext,crib,3)
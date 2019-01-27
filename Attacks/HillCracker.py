import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.HillCipher import hillCipher, createMatrixKey
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
    
    # If the crib is long enough try it in sections to find if they line up
    # properly.
    for pos in range(len(crib)-(N*N-1)):
        
        subCrib = cribN[pos:pos+(N*N)]
        
        A = Matrix(groups(subCrib,N)).T
        
        
        for i in range(len(G)-(N-1)):

            L = []
            for x in range(N):
                L.append(G[x+i])
                B = Matrix(L).T
            
        
            
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
                
    if bestKey.det() % 2 == 0 or bestKey.det() % 13 == 0:
        print("Something Strange Happened")
        print("Key Should be Inverse of:")
        pprint(bestKey)
        print()
    else:
        print("Key Is:")
        pprint(bestKey.inv_mod(26))
        print()
    
    print("Decrypt Looks Like:")
    print(hillCipher(ctext,bestKey))


def hillCipherAttackExample():
    
    print("""
The simple version of the Hill Cipher is very hard to break with access only to
the ciphertext. In order to attack it some piece of text from the plaintext,
known as a "crib", is needed. Here we will try to break the 3x3 version of the 
cipher using a few different cribs.
In order to make this work we have to try the crib in many positions and do a
relatively large amount of calculation. As a result we will try our attack on
just the first 300 characters.
""")
    
    # Load up the text to use
    textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\text1.txt', 'r')
    ptext = preptext1(textfile.readline(),silent=True)
    ptext = ptext[:300]
    #print(ptext,"\n\n")
    key = createMatrixKey(3)
    ctext = hillCipher(ptext,key)
    
    
    crib = "OTHERPART"
    
    hillCipherAttack(ctext,crib,3)
    
hillCipherAttackExample()
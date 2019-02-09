from Ciphers.HillCipher import hillCipher, createMatrixKey
from Ciphers.UtilityFunctions import groups
from sympy import Matrix, pprint
from Ciphers.PrepareText import preptext1
from Attacks.TextScoring import quadgramScore

def hillCipherCracker(ctext,crib,N):
    
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
        #print(subCrib)
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


def hillCipherCrackerExample():
    
    print("""
The simple version of the Hill Cipher is very hard to break with access only to
the ciphertext. In order to attack it some piece of text from the plaintext,
known as a "crib", is needed. Here we will try to break the 3x3 version of the 
cipher using a few different cribs.
In order to make this work we have to try the crib in many positions and do a
relatively large amount of calculation. As a result we will try our attack on
just the first 600 characters. If that fails we can try with the next section.
The minimum crib length is 9 but that will only work if the crib perfectly
lines up with a block. To ensure that we can decrypt the crib must have a
length of 17. A crib that long is not easy to get.
Suppose that we known this text is about sugar cane and we know the author has
the particular oddity of calling mollases "saccharine juice" from other things
we have seen written. We will try the following likely phrases:
THEWESTINDIES
THEISLANDS
THEMOLASSES
THESUGARCANE
SACCHARINEJUICE
""")
    
    # Load up the text to use
    textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\text1.txt', 'r')
    ptext = preptext1(textfile.readline(),silent=True)
    ptext = ptext[:600]
    key = createMatrixKey(3)
    ctext = hillCipher(ptext,key)
    print("Cipher Text:")
    print(ctext,"\n\n")
    
    
    cribs = ["THEWESTINDIES","THEISLANDS","THEMOLASSES","THESUGARCANE","SACCHARINEJUICE"]
    
    for crib in cribs:
        print("Using the crib: {}\n".format(crib))

        hillCipherCracker(ctext,crib,3)
        print("\n\n")
    
#hillCipherCrackerExample()
import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.HillCipher import hillCipher
from Ciphers.UtilityFunctions import groups
from sympy import Matrix, pprint
from Ciphers.PrepareText import preptext1
from Attacks.TextScoring import quadgramScore

def hillCipherAttack(ctext,crib):
    
    bestScore = quadgramScore(ctext)
    bestKey = Matrix([[1,1],[1,1]])
    
    # We can use this to reduce a matrix modulo 26
    mod26 = lambda x : x % 26
    
    # Convert the text and crib to numbers so they're more useful
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ctextN = [alpha.index(i) for i in ctext]
    cribN = [alpha.index(i) for i in crib]
    
    # Break text into pieces
    G = groups(ctextN,2)
    
    for pos in range(len(crib)-3):
        
        subCrib = cribN[pos:pos+4]
        
        #print(subCrib)
        
        A = Matrix([subCrib[:2],subCrib[2:]]).T
        
        for i in range(len(G)-1):
            B = Matrix([G[i],G[i+1]]).T
            
            # If the matrix is not invertible
            if B.det() % 2 == 0 or B.det() % 13 == 0:
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
                
                
    
    return hillCipher(ctext,bestKey)


# Load up the text to use
textfile = open('C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto\\SampleText\\text1.txt', 'r')
ptext = preptext1(textfile.readline(),silent=True)
ptext = ptext[:100]
ctext = hillCipher(ptext,[[23,20],[1,21]])


crib = "GREAT"

dtext = hillCipherAttack(ctext,crib)
print(dtext[:50])
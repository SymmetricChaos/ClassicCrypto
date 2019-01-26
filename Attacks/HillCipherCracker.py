import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.HillCipher import hillCipher
from Ciphers.UtilityFunctions import groups
from sympy import Matrix, pprint


def hillCipherAttack(ctext,crib):
    
    # We can use this to reduce a matrix modulo 26
    mod26 = lambda x : x % 26
    

    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ctextN = [alpha.index(i) for i in ctext]
    cribN = [alpha.index(i) for i in crib]
    
    # Break text into pieces
    G = groups(ctextN,2)
    
    print(G)
    
    A = Matrix([cribN[:2],cribN[2:]]).T
    
    for i in range(len(G)-1):
        B = Matrix([G[i],G[i+1]]).T
        
        if B.det() % 2 == 0:
            continue
        
        if B.det() % 13 == 0:
            continue
    
        C = A*(B.inv_mod(26))
        
        tKey = C.applyfunc(mod26)
    
        # We run the Hill Cipher in encryption mode NOT decryption
        print(hillCipher(ctext,tKey))

#ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
#ctext = hillCipher(ptext,[[23,20],[1,21]])

ctext = "FUPCMTGZKYUKBQFJHUKTZKKIXTTA"
crib = "FTHE"


hillCipherAttack(ctext,crib)
from Ciphers.Transposition import AMSCO
from Ciphers.Transposition.AMSCO import alternating
from Ciphers.UtilityFunctions import printColumns, uniqueRank

def AMSCOExample():
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    key = "BIRTH"
    rank = uniqueRank(key)
    
    al = alternating(ptext)
    
    print("   ".join([str(i) for i in rank]))
    printColumns(al,5,W=4)
    
    
    
    ctext = AMSCO(ptext,key)
    dtext = AMSCO(ctext,key,decode=True)
    print(ptext)
    print(ctext)
    print(dtext)

AMSCOExample()
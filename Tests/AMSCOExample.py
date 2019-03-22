from Ciphers.Transposition import AMSCO
from Ciphers.Transposition.AMSCO import alternating
from Ciphers.UtilityFunctions import printColumns, uniqueRank
from Tests.ExampleTemplate import example

def AMSCOExample():
    
    print("Example of the AMSCO Cipher")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    key = "BIRTH"
    rank = uniqueRank(key)
    
    al = alternating(ptext)
    
    print("\nThe Key Is {}\n".format(key))
    
    print("Each letter of the key is ranked to get")
    print(*rank)
    
    print("\nNow the text is read into the grid by rows as alternating letters and bigrams. The key is placed above.\n")

    
    print("   ".join([str(i) for i in rank]))
    printColumns(al,5,W=4)
    
    print("\nFinally the grid is read off in accordance with column numbers starting with zero, then one, and so on.\n")
    
    example(AMSCO,ptext,key)

AMSCOExample()
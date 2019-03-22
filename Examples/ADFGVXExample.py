from Ciphers.Polybius import ADFGVX
from Tests.ExampleTemplate import example

def ADFGVXExample():
    
    print("Example of the ADFGX Cipher\n")
    
    key = ["715ZEBRAS290","TABLES"]
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    
    print("They Polybius Square:")
    ADFGVX(ptext,key,printkey=True)
    print("\nThe Columnar Transport Key:")
    print(key[1],end="\n\n")

    example(ADFGVX,ptext,key)

ADFGVXExample()
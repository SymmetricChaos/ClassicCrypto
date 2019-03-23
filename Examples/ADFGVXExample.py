from Ciphers.Polybius import ADFGVX
from Examples.ExampleTemplate import example

def ADFGVXExample():
    
    print("Example of the ADFGVX Cipher\n")
    
    key = ["715ZEBRAS290","TABLES"]
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    
    print("The Polybius Square:")
    ADFGVX(ptext,key,printkey=True)
    print("\nThe Columnar Transport Key:")
    print(key[1],end="\n\n")

    ctext, dtext = example(ADFGVX,ptext,key)
    print(ctext)

ADFGVXExample()
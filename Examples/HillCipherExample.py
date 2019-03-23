from Ciphers.HillCipher import hillCipher, createMatrixKey
from sympy import pprint
from Examples.ExampleTemplate import example

def hillCipherExample():
    print("Example of the Hill Cipher\n")

    key = createMatrixKey(4)
    
    print("The key is:")
    pprint(key)
    print()
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    print(ptext)
    ctext, dtext = example(hillCipher,ptext,key)
    print(ctext)
    
    
hillCipherExample()
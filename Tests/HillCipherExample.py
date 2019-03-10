from Ciphers.HillCipher import hillCipher, createMatrixKey
from sympy import pprint
from Tests.ExampleTemplate import example

def hillCipherExample():
    print("Example of the Hill Cipher\n")

    key = createMatrixKey(4)
    
    print("The key is:")
    pprint(key)
    print()
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    example(hillCipher,ptext,key)
    
    
    
    print("\nUsing a Prime Alphabet")
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#"
    print("\nThe alphabet is\n{}\nWhich has length {}\n".format(alpha,len(alpha)))
    key = createMatrixKey(4,len(alpha))
    print("The key is:")
    pprint(key)
    print()
    
    example(hillCipher,ptext,key,alphabet=alpha)

hillCipherExample()
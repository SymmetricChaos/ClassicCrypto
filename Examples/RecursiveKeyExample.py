from Ciphers.Vigenere import recursiveKey
from Ciphers.UtilityFunctions import alphaToNumber, numberToAlpha
from Examples.ExampleTemplate import example

def recursiveKeyExample():

    print("Example of the Recursive Key Cipher")
    
    print("The recursive key cipher lengthens a short key by combining it with strentched out versions of itself.")
    
    print("Here the key is TABLE\n")
    
    k1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAATTTTT"
    k2 = "AAAAATTTTTAAAAABBBBBLLLLLEEEEETTTTT"
    k3 = "TABLETABLETABLETABLETABLETABLETABLE"
    n1 = alphaToNumber(k1)
    n2 = alphaToNumber(k2)
    n3 = alphaToNumber(k3)
    nT = [(a+b+c) % 26 for a,b,c in zip(n1,n2,n3)]
    kT = "".join(numberToAlpha(nT))
    k1 = "                              TTTTT"
    k2 = "     TTTTTAAAAABBBBBLLLLLEEEEETTTTT"
    k3 = "TABLETABLETABLETABLETABLETABLETABLE"
    print("{}\n{}\n{}\nWhich results in\n{}\n".format(k3,k2,k1,kT))

    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext, dtext = example(recursiveKey,ptext,"ZEBRAS")
    
    print(ptext)
    print(ctext)
    
    if dtext != ptext:
        print("Error")

recursiveKeyExample()
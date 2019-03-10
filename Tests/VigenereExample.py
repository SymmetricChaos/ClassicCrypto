from Ciphers.Vigenere import vigenere, multiVigenere, trithemius
from Ciphers.UtilityFunctions import lcm
from Tests.ExampleTemplate import example

def vigenereExample():

    print("Vigenere Example")
    key = "ZEBRAS"
    print("The Key Is: {}\n".format(key))
    
    print("Normal Mode")    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    example(vigenere,ptext,key)
    
    
def multiVigenereExample():

    print("Multiple Vigenere Example")
    key = ["ROMANCE","KINGDOMS"]
    print("The Key Is: {}".format(key))
    L = lcm( *[len(i) for i in key]  )
    print("Effective Key Length: {}\n".format(L))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    example(multiVigenere,ptext,key)
    
def trithemiusExample():
    print("Trithemius Example")
    print("The Key Is: ABCDEFGHIJKLMNOPQRSTUVWXYZ\n")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    example(trithemius,ptext,key="")
    
vigenereExample()
multiVigenereExample()
trithemiusExample()

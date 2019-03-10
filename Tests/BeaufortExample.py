from Ciphers.Vigenere import beaufort, multiBeaufort
from Ciphers.UtilityFunctions import lcm
from Tests.ExampleTemplate import example


def beaufortExample(ptext="THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"):

    print("Beaufort Example\n")
    key = "APPLES"
    print("The Key Is: {}\n".format(key))
    
    example(beaufort,ptext,key)
    

def multiBeaufortExample():

    print("Multiple Beaufort Example\n")
    key = ["AB","CDE","FGHIJ"]
    
    print("The Key Is: {}\n".format(key))
    
    L = lcm( *[len(i) for i in key] )
    print("Effective Key Length: {}\n".format(L))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    example(multiBeaufort,ptext,key)
        
beaufortExample()
multiBeaufortExample()
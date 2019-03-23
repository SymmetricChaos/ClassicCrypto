from Ciphers.Vigenere import beaufort, multiBeaufort
from Ciphers.UtilityFunctions import lcm
from Examples.ExampleTemplate import example

def beaufortExample():

    ptext="THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    
    print("Beaufort Example")
    key = "APPLES"
    print("The Key Is: {}\n".format(key))
    
    ctext, dtext = example(beaufort,ptext,key)
    print(ctext)

def multiBeaufortExample():

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    
    print("Multiple Beaufort Example")
    key = ["AB","CDE","FGHIJ"]
    
    print("The Key Is: {}".format(key))
    
    L = lcm( *[len(i) for i in key] )
    print("Effective Key Length: {}\n".format(L))
        
    ctext, dtext = example(multiBeaufort,ptext,key)
    print(ctext)
        
beaufortExample()
print()
multiBeaufortExample()
from Ciphers.Playfair import playfair,twoSquare, fourSquare
from Tests.ExampleTemplate import example

def playfairExample():
        
    print("Example of the Playfair\n")
    print("The key is:")
    key = "PLAYFAIREXAMPLE"
    playfair("",key,printkey=True,mode="IJ")
    
    print("")
    ptext = "THEQUICKBROWNFOXIUMPSOVERTHELAZYDOG"
    example(playfair,ptext,key)

    print("Example of the Two Square Version\n")
    print("The key is:")
    key = ["TWOSQUARE","CIPHER"]
    twoSquare("",key,printkey=True,mode="IJ")
    
    print("")
    ptext = "THEQUICKBROWNFOXIUMPSOVERTHELAZYDOG"
    example(twoSquare,ptext,key)
    
    print("Example of the Four Square Version\n")
    print("The key is:")
    key = ["TWOSQUARE","CIPHER"]
    fourSquare("",key,printkey=True,mode="IJ")
    
    print("")
    ptext = "THEQUICKBROWNFOXIUMPSOVERTHELAZYDOG"
    example(fourSquare,ptext,key)
    
playfairExample()
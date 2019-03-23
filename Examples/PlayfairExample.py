from Ciphers.Playfair import playfair
from Examples.ExampleTemplate import example

def playfairExample():
        

    key = "PLAYFAIREXAMPLE"
    ptext = "THEQUICKBROWNFOXIUMPSOVERTHELAZYDOG"
    
    print("Example of the Playfair\n")
    print("The key is the phrase {}\n".format(key))
    print("In a 5x5 grid skipping repeated letters and turning J into I we get this:\n")

    playfair("",key,printkey=True,mode="IJ")
    
    print("\nTo use this key we consider pairs of letters.\n")
    print("Letters in the same column are each replaced with the letter below. The pair EV turns into DA.")
    print("Letters in the same row are each replaced with the letter to the left. The pair KS turns into NK.")
    print("Otherwise read across from the first letter to the column of the second and vice versa. The pair TH becomes ZB.\n")
    
    print(ptext)
    ctext, dtext = example(playfair,ptext,key)
    print(ctext)

    
playfairExample()
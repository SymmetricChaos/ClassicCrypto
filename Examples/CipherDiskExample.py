from Ciphers import cipherDisk
from Ciphers.CipherDisk import stepN
import random
from ExampleTemplate import example
    
def cipherDiskExample():

    print("Example of a Cipher Disk\n")
    
    print("There disk has two rings. The outer ring is stationary while the inner ring can be turned and replaced by the user.")
    print("\nThe outer ring\nABCDEFGHIJKLMNOPQRSTUVQXYZ0123456789\n")
    
    inner = "1YW7USQ2OM8KIG3ECA9BD4FHJ0LNP5RTVX6Z"
    start = "K"
    inStart = inner[:]
    while inStart[0] != start:
        inStart = stepN(inStart,1)
    print("The inner ring\n{}\n".format(inner))
    
    print("The starting position for the inner ring is {} so it is rotated until {} is at the top position to get\n{}\n".format(start,start,inStart))
    
    random.seed(0)
    
    print("Encryption works like a simple substitution cipher but the operator can insert a number at any time then turn the inner disk by that many positions. This allows the cipher to change unpredictably.\n")
    
    key = [inner,start]
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    
    ctext, dtext = example(cipherDisk,ptext,key)
    
    print("{}\nbecomes\n{}".format(ptext,ctext))
    
cipherDiskExample()
from Ciphers import DRYAD
import random

def DRYADExample():
    print("Example of the DRYAD Cipher\n")
    keys = random.getrandbits(64)
    print("The key is {}\n".format(keys))
    ptext = "213165587194201"
    ctext = DRYAD(ptext,keys)
    dtext = DRYAD(ctext,keys,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
DRYADExample()
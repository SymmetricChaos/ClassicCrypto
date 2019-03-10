from Ciphers.Vigenere import beaufort, multiBeaufort
from Ciphers.UtilityFunctions import lcm

def beaufortExample():

    print("Beaufort Example\n")
    key = "APPLES"
    print("The Key Is: {}\n".format(key))
    
    print("Normal Mode")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = beaufort(ptext,key)
    dtext = beaufort(ctext,key)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    print("\nExtended Mode")
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = beaufort(ptext,key,alphabet=alpha)
    dtext = beaufort(ctext,key,alphabet=alpha)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
def multiBeaufortExample():

    print("Multiple Beaufort Example\n")
    key = ["ROMANCE","KINGDOMS"]
    print("The Key Is: {}\n".format(key))
    L = lcm( len(key[0]), len(key[1])  )
    print("Effective Key Length: {}\n".format(L))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = multiBeaufort(ptext,key)
    dtext = multiBeaufort(ctext,key,True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
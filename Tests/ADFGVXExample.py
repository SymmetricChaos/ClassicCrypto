from Ciphers.ADFGVX import ADFGVX

def ADFGVXExample():
    
    print("Example of the ADFGX Cipher\n")
    
    key = ["715ZEBRAS290","TABLES"]
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    
    print("They Polybius Square:")
    ADFGVX(ptext,key,printkey=True)
    print("\nThe Columnar Transport Key:")
    print(key[1],end="\n\n")

    ctext = ADFGVX(ptext,key)
    dtext = ADFGVX(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#ADFGVXExample()
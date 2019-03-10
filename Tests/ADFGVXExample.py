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
    print("{}".format(ptext))
    print("{}".format(ctext))
        
    if ptext != dtext:
        print("Decodes Error\n{}\n".format(dtext))

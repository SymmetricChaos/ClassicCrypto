from Ciphers.Autokey import autokey

def autokeyExample():

    print("Autokey Example\n")
    key = "APPLES"
    print("The Key Is: {}".format(key))
    
    for mode in ["vigenere","beaufort"]:
        print("\nIn {} mode".format(mode))
        ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
        ctext = autokey(ptext,key,mode=mode)
        dtext = autokey(ctext,key,decode=True,mode=mode)
        print("{}".format(ptext))
        print("{}".format(ctext))
        
        if ptext != dtext:
            print("Decodes Error\n{}\n".format(dtext))
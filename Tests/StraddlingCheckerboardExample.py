from Ciphers import straddlingCheckerboard

def straddlingCheckerboardExample():
    print("Example of the Straddling Checkerboard\n")
    keys = ["ZEBRA",[1,3]]
    print("The key is {}\n".format(keys))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = straddlingCheckerboard(ptext,keys)
    dtext = straddlingCheckerboard(ctext,keys,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
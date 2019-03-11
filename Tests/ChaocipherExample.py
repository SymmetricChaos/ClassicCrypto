from Ciphers import chaocipher
    
def chaocipherExample():
    print("Example of the Chaocipher\n")
    
    L = "HXUCZVAMDSLKPEFJRIGTWOBNYQ"
    R = "PTLNBQDEOYSFAVZKGJRIHWXUMC"


    print("The Left Alphabet:  {}".format(L))
    print("The Right Alphabet: {}".format(R))

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = chaocipher(ptext,[L,R])
    dtext = chaocipher(ctext,[L,R],decode=True)
    print("\nPlaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
chaocipherExample()
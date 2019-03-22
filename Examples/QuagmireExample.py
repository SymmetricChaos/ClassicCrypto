from Ciphers import quagmire1, quagmire2, quagmire3, quagmire4

def quagmireExample():
    print("Quagmire Examples\n")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    for cipher in [quagmire1,quagmire2,quagmire3]:
        
        print(cipher.__name__)
        
        key = ["ROMANCE","KINGDOMS"]
        print("The Key Is: {}".format(key))
        ctext = cipher(ptext,key,alphabet=alpha)
        dtext = cipher(ctext,key,decode=True,alphabet=alpha)
        
        if dtext != ptext:
            print("ERROR")
        
        print("Plaintext is:\n{}".format(ptext))
        print("Ciphertext is:\n{}\n".format(ctext))

    
    
    key = ["EXTRA","SENSORY","PERCEPTION"]
    ctext = quagmire4(ptext,key,alphabet=alpha)
    dtext = quagmire4(ctext,key,decode=True,alphabet=alpha)
        
    if dtext != ptext:
        print("ERROR")
    
    print("quagmire4")
    print("The Key Is: {}".format(key))
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}\n".format(ctext))
    
quagmireExample()
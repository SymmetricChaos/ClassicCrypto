def example(cipher,ptext,key,**kwargs):    
    ctext = cipher(ptext,key,False,**kwargs)
    dtext = cipher(ctext,key,True,**kwargs)
    print("{}".format(ptext))
    print("{}".format(ctext))
    if len(ptext) != len(ctext):
        print("Note that plaintext and cipher text differ in length.")
    if ptext != dtext[:len(ptext)]:
        print("Decodes Error\n{}\n".format(dtext))
    
    print("\n\n")

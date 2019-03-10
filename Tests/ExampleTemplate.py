def example(cipher,ptext,key,**kwargs):    
    ctext = cipher(ptext,key,False,**kwargs)
    dtext = cipher(ctext,key,True,**kwargs)
    print("{}".format(ptext))
    print("{}".format(ctext))
    if ptext != dtext:
        print("Decodes Error\n{}\n".format(dtext))
    print("\n")

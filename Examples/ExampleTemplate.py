def example(cipher,ptext,key,**kwargs):    
    ctext = cipher(ptext,key,False,**kwargs)
    dtext = cipher(ctext,key,True,**kwargs)
    if ptext != dtext[:len(ptext)]:
        print("DECRYPTION ERROR\n{}\n".format(dtext))
    
    return ctext, dtext

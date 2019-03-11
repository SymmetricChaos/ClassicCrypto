from Ciphers import hutton 

def huttonExample():
    ptext = "MEETMEATTHEGREENMANATTHREE"
    ctext = hutton(ptext,["FEDORA","JUPITER"])
    dtext = hutton(ctext,["FEDORA","JUPITER"],decode=True)
    
    print(ptext)
    print(ctext)
    print(dtext)
    
huttonExample()
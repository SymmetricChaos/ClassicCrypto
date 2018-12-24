from PolybiusSquare import polybiusSquare

# The nihilist cipher is a an composite cipher that uses the polybius square
# along with a modified vigenere cipher. Rather than wrapping around modulo 26
# addition and subtraction and performed normally.

def nihilistCipher(text,key=["A","A"],decode=False,mode="EX"):
    
    if mode == "EX":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    K = []
    for letter in key[1]:
        K.append(alphabet.index(letter))
    kLen = len(K)
    
    
    if decode == False:
    
        ps = polybiusSquare(text,key[0],mode=mode,sep=" ")
        nm = [int(p) for p in ps.split(" ")]
        
        for i in range(len(nm)):
            nm[i] = (nm[i]+K[i%kLen])
            
        return " ".join([str(i) for i in nm])
    
    if decode == True:
        
        nm = [int(p) for p in text.split(" ")]
        
        for i in range(len(nm)):
            nm[i] = (nm[i]-K[i%kLen])
        
        ps = " ".join([str(i) for i in nm])
        
        dtext = polybiusSquare(ps,key[0],decode=True,mode=mode,sep=" ")
            
        return dtext
        

#for md in ["CK","IJ","EX"]:
#    print(md)
#    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
#    ctext = nihilistCipher(ptext,["ZEBRA","PLOTS"],mode=md)
#    dtext = nihilistCipher(ctext,["ZEBRA","PLOTS"],decode=True,mode=md)
#    print(ptext)
#    print(ctext)
#    print(dtext)
#    print()
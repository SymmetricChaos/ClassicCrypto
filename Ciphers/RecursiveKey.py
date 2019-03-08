from Ciphers.UtilityFunctions import validptext, validkeys, alphaToNumber, numberToAlpha

def recursiveKey(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    
    # Validate the inputs
    validptext(text,alphabet)
    validkeys(key,[str,int])
    
    if len(set(alphabet)) != len(alphabet):
        raise Exception("Alphabet cannot repeat any symbols")
    
    K = alphaToNumber(key[0],alphabet)
    P = [0]*key[1]
    T = alphaToNumber(text,alphabet)
    M = len(alphabet)
  
    out = []
    
    for pos,textnum in enumerate(T,1):
        
        s = sum([K[i] for i in P])
        
        #print(numberToAlpha([K[i] for i in P],alphabet))
        
        if decode == False:
            out.append( (textnum+s) % M)
        else:
            out.append( (textnum-s) % M)
        
        for pwr in range(0,len(P)):
            if pos % (len(K)**pwr) == 0:
                P[pwr] = (P[pwr] + 1) % len(K)
        
    return "".join(numberToAlpha(out,alphabet))


def recursiveKeyExample():

    print("Example of the Progressive Key Cipher")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = recursiveKey(ptext,["TABLE",3])
    dtext = recursiveKey(ctext,["TABLE",3],decode=True)
    
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
recursiveKeyExample()
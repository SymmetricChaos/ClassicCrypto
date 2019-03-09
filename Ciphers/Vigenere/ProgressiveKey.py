from Ciphers.UtilityFunctions import validptext, validkeys, alphaToNumber, numberToAlpha
from itertools import cycle

def progressiveKey(text,key,decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    
    # Validate the inputs
    validptext(text,alphabet)
    validkeys(key,[str,int])
    
    
    if len(set(alphabet)) != len(alphabet):
        raise Exception("Alphabet cannot repeat any symbols")
    
    K = alphaToNumber(key[0],alphabet)
    pr = key[1]
    P = 0
    T = alphaToNumber(text,alphabet)
    M = len(alphabet)
  
    out = []
    
    for keynum,textnum in zip(cycle(K),T):
        
        if decode == False:
            out.append( (textnum+keynum+P) % M)
        else:
            out.append( (textnum-keynum-P) % M)
        
        if len(out) % len(K) == 0:
            P += pr
        
    return "".join(numberToAlpha(out,alphabet))


def progressiveKeyExample():

    print("Example of the Progressive Key Cipher")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = progressiveKey(ptext,["APPLE",3])
    dtext = progressiveKey(ctext,["APPLE",3],decode=True)
    
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
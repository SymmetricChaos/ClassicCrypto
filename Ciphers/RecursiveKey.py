from Ciphers.UtilityFunctions import validptext, validkeys, alphaToNumber, numberToAlpha
from itertools import cycle

def recursiveKey(text,key,decode=False,alphabet=""):
    
    if alphabet == "":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Validate the inputs
    validptext(text,alphabet)
    validkeys(key,[str,int])
    
    if len(set(alphabet)) != len(alphabet):
        raise Exception("Alphabet cannot repeat any symbols")
    
    K = alphaToNumber(key[0],alphabet)
    P = [0]*keyp[1]
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


def recursiveKeyExample():

    print("Example of the Progressive Key Cipher")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = recursiveKey(ptext,["APPLE",3])
    dtext = recursiveKey(ctext,["APPLE",3],decode=True)
    
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
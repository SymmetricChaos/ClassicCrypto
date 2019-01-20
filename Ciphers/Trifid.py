from itertools import product
from UtilityFunctions import alphabetPermutation, groups

# The trifid cipher is a slight variation on the bifid cipher that is intended
# to produce much greater degree of diffusion by splitting each letter into
# three digits rather than two.
    
def trifidCipher(text,key,decode=False):
    
    triplets = product("123",repeat=3)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ+"
    alphabet = alphabetPermutation(key,alphabet)
    D1 = {}
    D2 = {}
    
    for trip,alph in zip(triplets,alphabet):
        D1[alph] = "".join(trip)
        D2["".join(trip)] = alph
    
    if decode == False:

        A, B, C = "","","" 
        # Convert the letter into their triplets
        for letter in text:
            gr = D1[letter]
            A += gr[0]
            B += gr[1]
            C += gr[2]

        
        ctext = ""
        for gr in groups(A+B+C,3):
            ctext +=  D2[gr]
        
        return ctext
        

    if decode == True:
        grs = ""
        for letter in text:
            gr = D1[letter]
            grs += gr
        
        A = grs[:len(grs)//3]
        B = grs[len(grs)//3:2*len(grs)//3]
        C = grs[2*len(grs)//3:]
        
        dtext = [i+j+k for i,j,k in zip(A,B,C)]
        return "".join([D2[n] for n in dtext])
    

def trifidExample():
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    key = "AKEY"
    print("Example Of A Trifid Cipher\n\nKey is {}".format(key))

    ctext = trifidCipher(ptext,key)
    dtext = trifidCipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
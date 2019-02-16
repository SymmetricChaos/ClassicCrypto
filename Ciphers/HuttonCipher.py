from Ciphers.UtilityFunctions import alphabetPermutation

def swap(alpha,A,B):
    indA = alpha.index(A)
    indB = alpha.index(B)
        
    alpha[indA], alpha[indB] = alpha[indB], alpha[indA]


def hutton(text,keys=["",""],decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k1 = [alpha.index(i) + 1 for i in keys[0]]
    
    # Generate the initial alphabet then turn it into a list so it is easier to
    # manipulate by swapping letters.
    k2 = list(alphabetPermutation(keys[1]))

    out = ""
    
    if decode == False:
        for ctr,letter in enumerate(text):

            # Current position
            pos = k2.index(letter)
            # First increment, the alphabetic position of the first letter of the key
            inc1 = alpha.index(k2[0])+1
            # Second increment, the cyclic values from the first key aka "password"
            inc2 = k1[ctr%len(k1)]
            
            A = (pos+inc1+inc2) % 26
            
            out = out + k2[A]
            
            swap(k2,letter,k2[A])
    
    if decode == True:
        for ctr,letter in enumerate(text):
            
            # Current position
            pos = k2.index(letter)
            # First increment, the alphabetic position of the first letter of the key
            inc1 = alpha.index(k2[0])+1
            # Second increment, the cyclic values from the first key aka "password"
            inc2 = k1[ctr%len(k1)]
            
            A = (pos-inc1-inc2) % 26
            
            out = out + k2[A]
            
            swap(k2,letter,k2[A])
    
    return out
        
def huttonExample():
    ptext = "MEETMEATTHEGREENMANATTHREE"
    ctext = hutton(ptext,["FEDORA","JUPITER"])
    dtext = hutton(ctext,["FEDORA","JUPITER"],decode=True)
    
    print(ptext)
    print(ctext)
    print(dtext)
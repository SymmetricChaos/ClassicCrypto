from UtilityFunctions import alphabetPermutation

def substitution(text,key,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    
    # Derive the internally used key from the input
    KEY = alphabetPermutation(key)
            
    if decode == False:
        for i in text:
            out.append(KEY[alpha.index(i)])
    if decode == True:
        for i in text:
            out.append(alpha[KEY.index(i)])
    
    return "".join(out)

def rotate(R):
    return R[-1] + R[:-1]

def rotors(text,decode=False):
    R1 = "DMTWSILRUYQNKFEJCAZBPGXOHV"
    R2 = "HQZGPJTMOBLNCIFDYAWVEUSRKX"
    R3 = "UQNTLSZFMREHDPXKIBVYGJCWOA"
    
    out = []
    
    for letter in text:
        t = substitution(letter,R1)
        t = substitution(t,R2)
        t = substitution(t,R3)
        
        R1 = rotate(R1)
        if R1[0] == "Q":
            R2 = rotate(R2)
        if R2[0] == "E":
            R3 = rotate(R3)
        
        out.append(t)
    return "".join(out)
    
ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
ctext = rotors(ptext)
print(ctext)
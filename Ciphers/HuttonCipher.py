from Ciphers.UtilityFunctions import alphabetPermutation

def swap(alpha,A,B):
    indA = alpha.index(A)
    indB = alpha.index(B)
    
    t = list(alpha)
    
    t[indA], t[indB] = t[indB], t[indA]

    return "".join(t)

def hutton(text,keys=["",""],decode=True):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k1 = [alpha.index(i) + 1 for i in keys[0]]
    k2 = alphabetPermutation(keys[1])
    
    out = ""
    
    for ctr,letter in enumerate(text):
        pos = k2.index(letter)
        fst = alpha.index(k2[0])+1
        inc = k1[ctr%len(k1)]
        
        A = (pos+fst+inc) % 26
        
        out = out + k2[A]
        
        k2 = swap(k2,letter,k2[A])
    
    print(out)
        
    
hutton("MEETMEATTHEGREENMANATTHREE",["FEDORA","JUPITER"])
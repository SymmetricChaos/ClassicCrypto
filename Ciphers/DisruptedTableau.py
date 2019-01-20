import random
from UtilityFunctions import alphabetPermutation

# A continuously turning version of the cipher disk. Rather than keeping the
# same inner ring position until a change is inserted this version shifts the
# ring by one position each time. It also makes extra jumps when those are
# inserted.

# Step forward by N
def stepN(R,n):
    x = R[:]
    for i in range(n):
        x = x[1:] + x[0]
    return x

def disruptedTableau(text,key="",decode=False):
    
    outer = "ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789"
    
    if key == "":
        inner = "ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789"
    else:
        inner = alphabetPermutation(key,"ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789")


    if decode == False:
        out = ""
        for i in text:
            out += inner[outer.index(i)]
            if random.random() < .1:
                R = random.choice("123456789")
                out += inner[outer.index(R)]
                inner = stepN(inner,int(R))
            
            inner = stepN(inner,1)
            
        return out


    if decode == True:
        out = ""
        for i in text:
            dec = outer[inner.index(i)]
            
            inner = stepN(inner,1)
            if dec in "0123456789":
                inner = stepN(inner,int(dec))
            else:
                out += dec
        return out
    
def disruptedTableauExample():
    print("Example of a Disrupted Tableau\n")
    
    inner = "1YW7USQ2OM8KIG3ECA9BD4FHJ0LNP5RTVX6Z"

    print("Inner Ring Setting Is: {}\n".format(inner))

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = disruptedTableau(ptext,inner)
    dtext = disruptedTableau(ctext,inner,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
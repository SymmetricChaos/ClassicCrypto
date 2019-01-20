import random
from UtilityFunctions import alphabetPermutation

# Step a rotor forward by N
def stepN(R,n):
    x = R[:]
    for i in range(n):
        x = x[1:] + x[0]
    return x

# This cipher is based on the Alberti Cipher Disk. Encryption works as a
# simple substitution cipher. However the person encrypting can choose to shift
# the key of the cipher by encrypting a digit indicating the size of the shift
# they want. This computer implementation has a ten percent chance of shifting 
# the wheel after each letter. When decrypting one simply checks shfits the 
# cipher wheel whenever a digit is found.

# They key is simply the cipher wheel itself. In practice there should be a
# particular letter marked as a starting point. The shift away from the start
# can be a part of the key.

def cipherDisk(text,key="",decode=False):
    
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
                R = random.choice("0123456789")
                out += inner[outer.index(R)]
                inner = stepN(inner,int(R))

        return out


    if decode == True:
        out = ""
        for i in text:
            dec = outer[inner.index(i)]
            if dec in "0123456789":
                inner = stepN(inner,int(dec))
            else:
                out += dec
        return out



# A continuously turning version of the cipher disk. Rather than keeping the
# same inner ring position until a change is inserted this version shifts the
# ring by one position each time. It also makes extra jumps when those are
# inserted.

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

# The Chaocipher is a clever mechanical cipher that operates by creating a
# permutation of the alphabet rather than just shifting it.

def permuteL(L,letter):
    L = stepN(L,L.index(letter))
    L = L[0] + L[2:14] + L[1] + L[14:]
    return L
    
def permuteR(R,letter):
    R = stepN(R,R.index(letter)+1)
    R = R[0:2] + R[3:14] + R[2] + R[14:]
    return R

def chaocipher(text,keys=["",""],decode=False):
    
    if keys[0] == "":
        L = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
    else:
        L = keys[0]
    
    if keys[1] == "":
        R = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
    else:
        R = keys[1]
    
    if decode == False:
        out = ""
        for letter in text:
            pos = R.index(letter)
            out += L[pos]
            L = permuteL(L,L[pos])
            R = permuteR(R,letter)
        return out
    
    if decode == True:
        out = ""
        for letter in text:
            pos = L.index(letter)
            out += R[pos]
            L = permuteL(L,letter)
            R = permuteR(R,R[pos])
    
        return out 
    

def cipherDiskExample():

    print("Example of a Cipher Disk\n")
    
    inner = "1YW7USQ2OM8KIG3ECA9BD4FHJ0LNP5RTVX6Z"
    
    print("Inner Ring Setting Is: {}".format(inner))

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = cipherDisk(ptext,inner)
    dtext = cipherDisk(ctext,inner,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    

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
    

def chaocipherExample():
    print("Example of the Chaocipher\n")
    
    L = "HXUCZVAMDSLKPEFJRIGTWOBNYQ"
    R = "PTLNBQDEOYSFAVZKGJRIHWXUMC"


    print("The Left Alphabet:  {}".format(L))
    print("The Right Alphabet: {}".format(R))

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = chaocipher(ptext,[L,R])
    dtext = chaocipher(ctext,[L,R],decode=True)
    print("\nPlaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    

    

#cipherDiskExample()
#print("\n\n")
#disruptedTableauExample()
#print("\n\n")
#chaocipherExample()

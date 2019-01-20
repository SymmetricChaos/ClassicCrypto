import random
from UtilityFunctions import alphabetPermutation

# This cipher is based on the Alberti Cipher Disk. Encryption works as a
# simple substitution cipher. However the person encrypting can choose to shift
# the key of the cipher by encrypting a digit indicating the size of the shift
# they want. This computer implementation has a ten percent chance of shifting 
# the wheel after each letter. When decrypting one simply checks shfits the 
# cipher wheel whenever a digit is found.

# They key is simply the cipher wheel itself. In practice there should be a
# particular letter marked as a starting point. The shift away from the start
# can be a part of the key.

# Step forward by N
def stepN(R,n):
    x = R[:]
    for i in range(n):
        x = x[1:] + x[0]
    return x


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
import random
from Ciphers.UtilityFunctions import alphabetPermutation

# This cipher is based on the Alberti Cipher Disk. Encryption works as a
# simple substitution cipher. However the person encrypting can choose to shift
# the key of the cipher by encrypting a digit indicating the size of the shift
# they want.

# Choosing when the place the shifts is a trade off between security and the
# usability of the cipher. Short gaps are more secure but they make the 
# ciphertext longer and decoding more difficult. This implementation specifies
# a "gaprange" placing the next shift after between n and m letters.

# When decrypting one simply checks shfits the cipher wheel whenever a digit is
# found.

# They key is simply the cipher wheel itself. In practice there should be a
# particular letter marked as a starting point. The shift away from the start
# can be a part of the key.

# Step the inner disk forward by N
def stepN(R,n):
    x = R[:]
    for i in range(n):
        x = x[1:] + x[0]
    return x


def cipherDisk(text,key="",decode=False,gaprange=[6,8]):
    

    outer = "ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789"
    
    if key == "":
        inner = outer
    else:
        inner = alphabetPermutation(key,outer)

    out = []
    if decode == False:
        
        # Raise an error if there are digits in the plaintext since they will
        # cause decoding errors.
        for i in "0123456789":
            if i in text:
                raise Exception("Cannot include numbers in the plaintext.")
        
        
        gap = random.randint(gaprange[0],gaprange[1])
        for i in text:
            out.append( inner[outer.index(i)] )
            gap -= 1
            if gap == 0:
                R = random.choice("0123456789")
                out += inner[outer.index(R)]
                inner = stepN(inner,int(R))
                gap = random.randint(gaprange[0],gaprange[1])

    if decode == True:
        for i in text:
            dec = outer[inner.index(i)]
            if dec in "0123456789":
                inner = stepN(inner,int(dec))
            else:
                out.append(dec)
    
    return "".join(out)


    
def cipherDiskExample():

    print("Example of a Cipher Disk\n")
    
    inner = "1YW7USQ2OM8KIG3ECA9BD4FHJ0LNP5RTVX6Z"
    
    print("Inner Ring Setting Is:\n{}\n".format(inner))

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = cipherDisk(ptext,inner)
    dtext = cipherDisk(ctext,inner,decode=True)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    print("Decodes As:\n{}".format(dtext))
    
cipherDiskExample()
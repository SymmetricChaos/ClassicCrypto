from Ciphers.Polybius.Polybius import polybiusSquare

# The bifid cipher is a very simple composite cipher that uses the polybius
# square followed by a simple transposition followed by the polybius square
# in reverse.

def bifid(text,key,decode=False):
    
    """
:param text: The text to be encrypyed. Must be uppercase.
:param key: A keyword that is used to encrypt the text.
:param decode: Boolean. If false encrypt plaintext. If true decode ciphertext
    """
    
    nums = polybiusSquare(text,key)

    if decode == False:
  
        A = ""
        B = ""
        for i in range(len(text)):
            A += nums[i*2]
            B += nums[i*2+1]
        return polybiusSquare(A+B,key,decode=True)

    if decode == True:
        A = nums[:len(nums)//2]
        B = nums[len(nums)//2:]
        out = "".join([i+j for i,j in zip(A,B)])
    
        return polybiusSquare(out,key,decode=True)


def bifidExample():

    print("Bifid Cipher Example\n")
    key = "SWANSAREBIRDS"
    print("The Key Is: {}\n".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = bifid(ptext,key)
    dtext = bifid(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    
#bifidExample()
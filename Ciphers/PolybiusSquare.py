from itertools import product
from UtilityFunctions import alphabetPermutation, groups
from Transposition import columnarTransport

# The polybius square is a way of converting each letter of an alphabet into a
# a pair of numbers. In order for this to work the size of the alphabet should
# be close to a square number. There are three commons ways to do this. 
# Replace the uncommon letter J with the common letter I that looks similar.
# Replace the letter C with the letter K which is pronounced similarly. 
# Extend the alphabet with the ten digits.
# This cipher uses the extended alphabet as the default.

# Technically the polybiusSquare is just a simple substitution cipher. However
# it is extremely useful in other ciphers.

# The "sep" keyword allows the symbol that separates the codegroups of the
# polybius square. By default there is no separation at all. This setting is
# useful for better readbility or the nihilist cipher.

def polybiusSquare(text,key="",decode=False,mode="EX",sep=""):
    #the IJ version of the polybius (25 characters)
    if mode == "IJ":
        alpha = "ABCEDFGHIKLMNOPQRSTUVWXYZ"
        text = text.replace("J","I")
        key = key.replace("J","I")

    #the CK version of the polybius (25 characters)
    if mode == "CK":
        alpha = "ABEDFGHIJKLMNOPQRSTUVWXYZ"
        text = text.replace("C","K")
        key = key.replace("C","K")
        
    #the KQ version of the polybius (25 characters)
    if mode == "KQ":
        alpha = "ABCEDFGHIJKLMNOPRSTUVWXYZ"
        text = text.replace("Q","K")
        key = key.replace("Q","K")   
        
    #the extended version of the polybius (36 characters)
    if mode == "EX":
        alpha = "ABCEDFGHIJKLMNOPQRSTUVWXYZ0123456789"

    
    # Generate the internal key using user key
    k = alphabetPermutation(key,alphabet=alpha)

    if mode == "EX":
        codegroups = ["".join(i) for i in product("123456",repeat=2)]
    else:
        codegroups = ["".join(i) for i in product("12345",repeat=2)]
        

    if decode == False:
        # Pair each letter with a codegroup
        D = {}
        for i,j in zip(k,codegroups):
            D[i] = j
        
        ctext = [D[let] for let in text]
    
        return sep.join(ctext)
    
    if decode == True:
        # Pair each codegrou with a letter
        D = {}
        for i,j in zip(k,codegroups):
            D[j] = i
        if sep != "":
            grps = text.split(sep)
        else:
            grps = [text[2*j:2*j+2] for j in range(len(text)//2)]
        dtext = [D[pair] for pair in grps]
    
        return "".join(dtext)
    
    
# The nihilist cipher is a composite cipher that uses the polybius square
# along with a modified vigenere cipher. Rather than wrapping around modulo 26
# addition and subtraction and performed normally.
def nihilistCipher(text,key=["A","A"],decode=False,mode="EX"):
    
    # Convert the vigenere key into numbers using the polybius square
    keynum = polybiusSquare(key[1],key[0],mode=mode,sep=" ")
    keynum = [int(n) for n in keynum.split(" ")]
    kLen = len(keynum)
    
    if decode == False:
        
        textnum = polybiusSquare(text,key[0],mode=mode,sep=" ")
        textnum = [int(n) for n in textnum.split(" ")]


        for i in range(len(textnum)):
            textnum[i] = (textnum[i]+keynum[i%kLen])
        
        return " ".join([str(i) for i in textnum])
    
    if decode == True:
        
        textnum = [int(n) for n in text.split(" ")]
        
        for i in range(len(textnum)):
            textnum[i] = (textnum[i]-keynum[i%kLen])
        
        textnum = " ".join([str(i) for i in textnum])
        
        dtext = polybiusSquare(textnum,key[0],decode=True,mode=mode,sep=" ")
            
        return dtext
    
# The bifid cipher is a very simple composite cipher that uses the polybius
# square followed by a simple transposition followed by the polybius square
# in reverse.

def bifidCipher(text,key,decode=False):
    
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
    

# The ADFGX cipher is an important early example of a fractionated cipher that
# produces Shannon's "confusion" in the ciphertext. That is the symbols of the
# ciphertext depend on many parts of the plaintext.
        
# A modified polybius square is used. Historically it used ADFGX rather than 
# 12345, hence the name.

# A significantly more secure cipher is the ADFGVX variant which extends the
# alphabet to also contain numbers. This allows shorter messages that give the
# attacker less to work with.

def ADFGX(text,keys=["A",[0,1]],decode=False):
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alpha = alphabetPermutation(keys[0],alpha)
    
    # Replace 
    text = text.replace("J","I")
    
    pairs = product("ADFGX",repeat=2)
    
    D1 = {}
    D2 = {}
    for letter,pair in zip(alpha,pairs):
        D1[letter] = "".join(pair)
        D2["".join(pair)] = letter

    # The ADFGX cipher has a roughly symmetric encode and decoding process
    # the only difference is that the columnar transport is reversed.

    # Turn every letter into a pair of symbols
    ctext = "".join([D1[i] for i in text])
    # Scramble the symbols, this will break apart some of the pairs
    ctext = columnarTransport(ctext,keys[1],decode=decode)
    # Now take the scrambled symbols and turn them back into letters
    ctext = groups(ctext,2)
    ctext = "".join([D2[i] for i in ctext])

    return ctext

def ADFGVX(text,keys=["A",[0,1]],decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    alpha = alphabetPermutation(keys[0],alpha)
    
    pairs = product("ADFGVX",repeat=2)
    
    D1 = {}
    D2 = {}
    for letter,pair in zip(alpha,pairs):
        D1[letter] = "".join(pair)
        D2["".join(pair)] = letter

    # Turn every letter into a pair of symbols
    ctext = "".join([D1[i] for i in text])
    # Scramble the symbols, this will break apart some of the pairs
    ctext = columnarTransport(ctext,keys[1],decode=decode)
    # Now take the scrambled symbols and turn them back into letters
    ctext = groups(ctext,2)
    ctext = "".join([D2[i] for i in ctext])

    return ctext
    
def ADFGXexample():

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = ADFGX(ptext,["ZEBRAS",[1,4,2,5,0,3]])
    dtext = ADFGX(ctext,["ZEBRAS",[1,4,2,5,0,3]],decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    

def ADFGVXexample():

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = ADFGVX(ptext,["17ZEBRAS529",[1,4,2,5,0,3]])
    dtext = ADFGVX(ctext,["17ZEBRAS529",[1,4,2,5,0,3]],decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))


def polybiusSquareExample():
    ptext = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
    key = "FIVEZEBRAS"
    print("Example Of A Polybius Square\n\nKey is {}\n".format(key))
    
    print("Plaintext is:  {}\n\n".format(ptext))
    
    for mode in ["IJ","CK","KQ","EX"]:
        print("Using Mode {}".format(mode))
        ctext = polybiusSquare(ptext,key,mode=mode,sep=" ")
        print("Ciphertext is: {}".format(ctext))
        dtext = polybiusSquare(ctext,key,decode=True,mode=mode,sep=" ")
        print("Decodes As:    {}".format(dtext))
        print()

def trifidExample():
    ptext = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
    key = "AKEY"
    print("Example Of A Trifid Cipher\n\nKey is {}\n".format(key))

    ctext = trifidCipher(ptext,key)
    dtext = trifidCipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    
def nihilistCipherExample():
    ptext = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
    key = ["SOMETHING","NIHILIST"]
    print("Example Of The Nihilist Cipher\n\nKey is {}\n".format(key))

    mode = "KQ"
    print("Plaintext is:  {}".format(ptext))
    ctext = nihilistCipher(ptext,key,mode = mode)
    print("Ciphertext is: {}".format(ctext))
    dtext = nihilistCipher(ctext,key,decode=True, mode = mode)
    print("Decodes As:    {}".format(dtext))

#polybiusSquareExample()
nihilistCipherExample()
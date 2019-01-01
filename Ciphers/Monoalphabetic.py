from UtilityFunctions import alphabetPermutation, modinv

# Monoalphabetic ciphers transform every letter in the message using exactly
# the same method. There are three methods provided here plus the atbash which
# is a special case of the general substitution cipher.



# The caesar cipher, named after Julius Caesar who is said to have used it to
# protect his military secrets. Every letter is shifted a certain number of
# positions along the alphaet. So for a caesar cipher with a key of 3 the
# the letter A becomes D, while M becomes P, and X becomes A. To decode the
# cipher the letters are shifted back. The popular ROT13 is simply the caesar
# cipher with a key of 13.

def caesar(text,key,decode=False):
    text = text.upper()
    
    if decode == True:
        key = 26-key
        
    out = []
    for i in text:
        # Convert each letter to a numeric value the 65 is there because the
        # ASCII values for capital letters start there
        val = ord(i)-65
        # Shift the number by the key value
        val = (val + key) %26
        # Convert back to a letter
        out.append(chr(val+65))
    return "".join(out)
        
# Yes we could do this in one line as
# return "".join([chr((ord(i)-65+key)%26+65) for i in text])
# But these ciphers are meant to be easy to read,




# The affine cipher is very similar but requires more of an understanding of
# modular arithmetic. Each letter is assigned a number with A = 0, B = 1, and
# so on. Then each number has a value added to it and it multiplied by a value.
# The result is reduced modulo 26. Then the numbers are turned back into
# letters using the same rules 0 = A, 1 = B, 2 = C.

def affine(text,key=[0,1],decode=False):
    
    # In this basic form of affine cipher the multiplication cannot be a
    # multiple of 2 or 13 since they have no inverse modulo 26.
    if key[1] % 2 == 0:
        raise Exception('multiplicative part has no inverse')
    if key[1] % 13 == 0:
        raise Exception('multiplicative part has no inverse')
    
    T = []
    
    for i in text:
        N = ord(i)-65
        
        if decode == False:
            N = (N+key[0])%26
            N = (N*key[1])%26
        else:
            inv = modinv(key[1],26)
            N = (N*inv)%26
            N = (N-key[0])%26
        
        T.append(chr(N+65))
        
    return "".join(T)



# The general substitution cipher. It simple replaces letters
# with other letters. To make this easier the key may be any sequence of
# letters from the English alphabet. The letter A is turned into to the first
# letter of the word, the letter B is turned into the second letter of the
# word and so on. If the word repeats letters those repetitions are skipped.

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



# The atbash cipher is a special case of the substitution cipher that just uses
# a reversed alphabet. Since it has no key it is not a true cipher.

def atbash(text,decode=False):
    return substitution(text,"ZYXWVUTSRQPONMLKJIHGFEDCBA",decode=decode)
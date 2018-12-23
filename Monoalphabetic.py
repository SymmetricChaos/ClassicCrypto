from ModularArithmetic import modinv

# Monoalphabetic ciphers transform every letter in the message using exactly
# the same method. There are three methods provided here.

# The casar cipher, named after Julius Caesar who is said to have used it to
# protect his military secrets. Every letter is shifted a certain number of
# positions along the alphaet. So for a caesar cipher with a key of 3 the
# the letter A becomes D, while M becomes P, and X becomes A. To decode the
# cipher the letters are shifted back.

# The affine cipher is very similar but requires more of an understanding of
# modular arithmetic. Each letter is assigned a number with A = 0, B = 1, and
# so on. Then each number has a value added to it and it multiplied by a value.
# The result is reduced modulo 26. Then the numbers are turned back into
# letters using the same rules 0 = A, 1 = B, 2 = C.

# The final cipher is a general substitution cipher. It simple replaces letters
# with other letters. To make this easier the key may be any sequence of
# letters from the English alphabet. The letter A is turned into to the first
# letter of the word, the letter B is turned into the second letter of the
# word and so on. If the word repeats letters those repetitions are skipped.

def caesar(s,k,decode=False):
    s = s.upper()
    if decode == True:
        k = 26-k
    return "".join([chr((ord(i)-65+k)%26+65) for i in s])

def affine(s,k=[0,1],decode=False):
    
    # In this basic form of affine cipher the multiplication cannot be a
    # multiple of 2 or 13 since they have no inverse modulo 26.
    if k[1] % 2 == 0:
        raise Exception('multiplicative part has no inverse')
    if k[1] % 13 == 0:
        raise Exception('multiplicative part has no inverse')
    
    T = []
    
    for i in s:
        N = ord(i)-65
        
        if decode == False:
            N = (N+k[0])%26
            N = (N*k[1])%26
        else:
            inv = modinv(k[1],26)
            N = (N*inv)%26
            N = (N-k[0])%26
        
        T.append(chr(N+65))
        
    return "".join(T)

def substitution(s,k,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    
    # Derive the internally used key from the input
    # We use only the unique letters of the key and then
    # follow them with the remaining letters of the alphabet
    key = ""
    for letter in k:
        if letter not in key:
            key += letter
    for letter in alpha:
        if letter not in key:
            key += letter
            
    if decode == False:
        for i in s:
            out.append(key[alpha.index(i)])
    if decode == True:
        for i in s:
            out.append(alpha[key.index(i)])
    
    return "".join(out)



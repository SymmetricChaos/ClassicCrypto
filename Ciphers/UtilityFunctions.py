###############################################################################
## A bunch of functions we need for various reasons kept here for neatness.  ##
###############################################################################


# Many ciphers need to create a permutation of the alphabet. A common way to do
# this for classical cryptography is to specify a key. The letters of the key
# are form the beginning of the new alphabet, skipping any repetition, and then
# the remaining letters of the alphabet are placed in order after them.

# For example the keyword CRYPTOGRAM produces the alphabet
# CRYPTOGAMBDEFHIJKLNQSUVWXZ

def alphabetPermutation(key,alphabet=""):
    if alphabet == "":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Include every unique letter of the key in the order it appears
    k = ""
    for letter in key:        
        if letter not in alphabet:
            raise Exception('key does not fit with alphabet')
        if letter not in k:
            k += letter
    # Put in every unused letter of the alphabet into the key
    for letter in alphabet:
        if letter not in k:
            k += letter
    
    return k

# A very simple function for testing if inputs matches output
def decodetest(text,keys,fun):
    ctext = fun(text,keys)
    dtext = fun(ctext,keys,decode=True)
    if text == dtext[:len(text)]:
        print("Success With {}".format(fun.__name__))
    else:
        raise Warning("Decode Error With {}".format(fun.__name__))


# Return a list of groups from the text
# For example
# groups("ABCDEFGHIJKL",3)
# ["ABC","DEF","GHI","JKL"]
def groups(text,n):     
    return [text[i*n:i*n+n] for i in range(len(text)//n)]


## Get prime numbers.
def primes():
    D = {}
    q = 2
    while True:
        if q not in D:

            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

# This is an excessively simple way of finding all the factors btu we're only
# using it on very small numbers.
def factors(n):
    L = []
    for i in range(2,n):
        if n % i == 0:
            L.append(i)
    return L

# Extended Euclidean algorithm
# Return greatest common denominator and the numbers x and y such that
# g = ax + by
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Use egcd to calculate the modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Use egcd to calculate the least common multiple
def lcm(a,b):
    g,x,y = egcd(a,b)
    return abs(a*b)//g

# Unique rank for each element of a list
# Uses two dictionaries and a counter.
# First the list is sorted then it is stepped through symbol by symbol
# At each symbol in the list the counter goes up by one.
# If it is new the symbol is added to the 'a' and 'b' dictionaries
# If it is old its value in the 'b' dictionary is increased
# Then when ranking we subtract the 'b' value of the symbol from the greatest
# 'b' value it reach, then decrement the 'b' value
def uniqueRank(text):
    a={}
    b={}
    rank=0
    for num in sorted(text):
        if num in b:
            b[num] += 1
            rank=rank+1
        if num not in a:
            a[num] = rank
            b[num] = 0
            rank=rank+1
    out = []
    bmax = b.copy()
    for i in text:
        out.append(a[i]+bmax[i]-b[i])
        b[i] -= 1
    return out

# Delete any spaces at the end of the text
def removeTrailingSpaces(text):
    while text[-1] == " ":
        text = text[:-1]
    return text

# Generator that returns each position where a substring exists
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

# Create the squares used for polybius squares and playfair
def makeSquare(key,mode):
    
    # Prep the key and derive the alphabet
    if mode == "IJ" or mode == "JI":
        key = key.replace("J","I")
        k = alphabetPermutation(key,"ABCDEFGHIKLMNOPQRSTUVWXYZ")
    if mode == "CK" or mode == "KC":
        key = key.replace("C","K")
        k = alphabetPermutation(key,"ABDEFGHIJKLMNOPQRSTUVWXYZ")
    if mode == "KQ" or mode == "QK":
        key = key.replace("Q","K")
        k = alphabetPermutation(key,"ABCDEFGHIJKLMNOPRSTUVWXYZ")
    if mode == "EX":
        k = alphabetPermutation(key,"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    
    
    if mode == "EX":
        g = groups(k,6)
        sq = []
        for i in g:
            sq.append([x for x in i])
        return sq

    else:
        g = groups(k,5)
        sq = []
        for i in g:
            sq.append([x for x in i])
        return sq

def squareIndex(sq):
    D = {}
    for i,row in enumerate(sq):
        for j,letter in enumerate(row):
            D[letter] = (i,j)
    return D

import re

def preptext(text,keepSpaces=False,keepDigits=False,silent=False):

    # Remove anything that isn't an alphanumeric character. Keep spaces if
    # requested.
    if silent == False:
        print("REMOVING NON-ALPHANUMERIC CHARACTERS")
    if keepSpaces == False:
        T = re.sub(r'[^a-zA-Z0-9]', '', text)
        if silent == False:
            print("REMOVING SPACES")
    else:
        T = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    
    # Convert digits into names
    if keepDigits == False:
        if silent == False:
            print("DIGITS REPLACED WITH NAMES")

        for i,j in zip(range(10),["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]):
            T = re.sub(r'[{}]'.format(i), j, T)

    # Convert letters to uppercase
    if silent == False:
        print("CONVERTING TO UPPERCASE")        
    T = T.upper()
    
    return T

def playfairPrep(text,mode="IJ"):

    if mode == "IJ":
        text = text.replace("J","I")
    if mode == "CK":
        text = text.replace("C","K")
    if mode == "KQ":
        text = text.replace("Q","K")
    if mode == "EX":
        pass
        
    # chn just checks if we changed anything
    # At the start of each while loop set it to zero assuming we won't change
    # anything. Then as we step through the text if we find a double letter
    # that might mess up playfair cipher fix it then start from the beginning.
    chn = 1
    while chn == 1:
        
        chn = 0
        for i in range(len(text)//2):
            x = text[i*2:i*2+2]
            if x[0] == x[1]:
                if x[0] != "X":
                    text = text[:i*2+1] + "X" + text[i*2+1:]
                    chn = 1
                    break
                else:
                    text = text[:i*2+1] + "Z" + text[i*2+1:]
                    chn = 1
                    break
                
    # Make sure the are an even number of letters
    if len(text) % 2 == 1:
        if text[-1] != "Z":
            text += "Z"
        else:
            text += "X"
    return text

# Plaintext must have specific form which we can check for.
def validptext(T,alpha):
    if type(T) != str:
        raise Exception("Plaintext must be a string")
    
    for i in T:
        if i not in alpha:
            raise Exception("{} is not a valid plaintext character".format(i))

# Keys must also have specific form which we can check for.
def validkeys(K,types):
    
    if type(types) != list:
        if type(K) != types:
            raise Exception("Key must be {}".format(types))
    
    
    else:
        for pos,pair in enumerate(zip(K,types),1):

            if type(pair[0]) != pair[1]:
                raise Exception("Key #{} must be {}".format(pos,pair[1]))


# Clever recursive function that converts decimal numbers to another base (not my work)
# Returns a string not a number
def baseConvert(n,base=10,bigendian=False):
    if base < 1:
        raise Exception("Base cannot be less than 1")
    if base > 36:
        raise Exception("Base cannot be greater than 36")
        
    if base == 1:
        return "1"*n
        
    vals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < base:
        return vals[n]
    else:
        return baseConvert(n//base,base) + vals[n%base]

# Convert a string in a given base to a decimal number
def str2dec(s,base=2):
    
    if base < 1:
        raise Exception("Base cannot be less than 1")
    if base > 36:
        raise Exception("Base cannot be greater than 36")
        
    
    
    vals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    out = 0
    s = s[::-1]
    for n,b in enumerate(s):
        out += base**n * vals.index(b)
    return out


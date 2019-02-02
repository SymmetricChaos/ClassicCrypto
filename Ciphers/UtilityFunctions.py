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

# Functions for doing modular arithmetic.
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
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

def removeTrailingSpaces(text):
    while text[-1] == " ":
        text = text[:-1]
    return text


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
        
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

###############################################################################
## A bunch of functions we need for various reasons kept here for neatness.  ##
###############################################################################


import re
import random

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
            raise Exception('{} is not in the alphabet'.format(letter))
        if letter not in k:
            k += letter
    # Put in every unused letter of the alphabet into the key
    for letter in alphabet:
        if letter not in k:
            k += letter
    
    return k

# A very simple function for testing if inputs matches output
def decodetest(fun,text,keys,**kwargs):
    ctext = fun(text,keys,**kwargs)
    dtext = fun(ctext,keys,decode=True,**kwargs)
    if text == dtext[:len(text)]:
        print("Success With {}".format(fun.__name__))
    else:
        raise Warning("Decode Error With {}".format(fun.__name__))


# Return a list of groups from the text
# For example
# groups("ABCDEFGHIJKL",3)
# ["ABC","DEF","GHI","JKL"]
# groups("ABCDEFGHIJK",3)   
# ["ABC","DEF","GHI","JK"]
def groups(text,n):
    if len(text) % n == 0:
        return [text[i*n:i*n+n] for i in range(len(text)//n)]
    else:
        return [text[i*n:i*n+n] for i in range(len(text)//n+1)]

## Generator that returns primes (not my work)
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
# using it on very small numbers. Can be set to return prime factors.
def factors(n,prime=False):
    L = []
    
    # If not in primes mode just check all the numbers
    if prime == False:
        for i in range(2,n+1):
            if n % i == 0:
                L.append(i)
        return L
    
    # If it is in primes mode check all primes
    else:
        for i in primes():
            if i > n:
                break
            if n % i == 0:
                L.append(i)
        return L


# Extended Euclidean algorithm
# g   : Greatest common denominator
# x,y : integers such that g = ax + by
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

# Use egcd calculate the least common multiple
def lcm(*args):
    
    # simplest case
    if len(args) == 1:
        return args[0]
    
    # calculate lcm for two numbers
    if len(args) == 2:
        a = args[0]
        b = args[1]
        g,x,y = egcd(a,b)
        return abs(a*b)//g
    
    # if more than two break it up recursively
    a = lcm(*args[0:2])
    b = lcm(*args[2:])
    return lcm(a,b)

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


def digitsToNames(text):
    
    # Give each digit its name
    for i,j in zip(range(10),["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]):
        text = re.sub(r'[{}]'.format(i), j, text)
    return text


def preptext(text,keepSpaces=False,keepDigits=False,keepCase=False,silent=False):

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
        T = digitsToNames(T)
        
    # Convert letters to uppercase
    if keepCase == False:
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


# Make sure the alphabet is an made of unique letters
def validalpha(alphabet):
    if len(set(alphabet)) != len(alphabet):
        raise Exception("Alphabet cannot repeat any symbols")
    

# Clever recursive function that converts decimal numbers to another base (not my work)
# Returns a string not a number.
def baseConvert(n,base=10):
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


# Find all the characters which are not part of a given alphabet and save what
# they are and where they go.
def saveFormat(S,alphabet = ""):
    
    if alphabet == "":
       alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    final,case = [], []
    
    pos, char = [], []
    for ps,ch in enumerate(S):
        if ch not in alphabet:
            char.append(ch)
            pos.append(ps)
        else:
            final.append(ch.upper())
            case.append(ch.isupper())
    return "".join(final), pos, char, case


# Use the output of saveChars to put the characters back where they used to be
def restoreFormat(S,pos,char,case):
    
    T = [i for i in S]
    for ps,ca in enumerate(case):
        if T[ps].isupper() != ca:
            if ca:
                T[ps] = T[ps].upper()
            else:
                T[ps] = T[ps].lower()

    S = "".join(T)
    
    for ps,ch in zip(pos,char):
        S = S[:ps] + ch + S[ps:]
    return S


# Given a list and a number of columns print the list into
# that many columns. If desired specifiy a width for the
# columns.
def printColumns(L,N,W=0):
    
    # By default assume all are the same width and with one space
    if W == 0:
        W = len(str(L[0]))+1
    
    for ctr,element in enumerate(L,1):
        s = "{: <{}}".format(str(element),W)
        print(s,end="")
        if ctr % N == 0 or ctr == len(L):
            print()


# Convert letters to numbers according to some alphabet
def alphaToNumber(L,alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return [alpha.index(i) for i in L]


# Convert numbers to letters according to some alphabet
def numberToAlpha(L,alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return [alpha[i] for i in L]

# Append nulls to fill out text to a given length. First the characters of the 
# seperator are appended and then random letters from an alphabet.
def addNulls(text,total_len,sep="XXX",alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    
    ctr = 0
    while len(text) < total_len:
        
        if ctr >= len(sep):
            text += random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        else:
            text += sep[ctr]
            ctr += 1
    
    return text
    
    
    
    
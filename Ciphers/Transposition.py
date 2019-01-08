## A transposition cipher is made by shuffling the letters of the message
## according to some rule. One of the most famous transposition ciphers is
## columnar transport. To do this the message is read into a matrix by rows
## then the columns of the matrix are suffled and read off by columns.

## The order of the arguments
from numpy import argsort
from numpy.random import choice
from UtilityFunctions import uniqueRank, groups

def columnarTransport(text,key,decode=False):
    
    k = uniqueRank(key)
    
    ## Add nulls if necessary
    # The nulls are uncommon consonants so that they cannot accidentally form
    # words at the end of the true message
    numcol = len(k)
    numrow,rem = divmod(len(text),numcol)
    if rem != 0:
        text += "".join(choice(["Z","Q","J","X","V","W"],numcol-rem))
        numrow += 1

    ## In case of decrypting
    if decode == True:
        L = []
        for i in range(numrow):
            L.append(text[i::numrow])
            
        out = ""
        for i in L:
            for j in k:
                out += i[j]
        
        return out 
    if decode == False:
        ## Create the rows
        L = []
        for i in range(numrow):
            L.append(text[i*numcol:numcol+i*numcol])
        
        ## Read the columns 
        out = ""
        for x in argsort(k):
            out += "".join([i[x] for i in L])
            
        return out

### Double columnar transport is a significant improvement on the single columnar
### transport cipher. With long keys it is even somewhat resistant to computer attack.

def doubleColumnarTransport(text,key=["ABC","ABC"],decode=False):
    if len(key) != 2:
        raise Exception("Must have exactly two keys")
    while len(key[0]) > len(key[1]):
        key[1] += "Z"
    while len(key[1]) > len(key[0]):
        key[0] += "Z"
    if decode == True:
        return columnarTransport(columnarTransport(text,key[1],True),key[0],True)
    else:
        return columnarTransport(columnarTransport(text,key[0]),key[1])

# The rail fence cipher is a transposition cipher than writes the letters of
# plaintext up and down the rails of an imaginary fence then reads the rails
# one at a time.

# So for three rails the sentence
# THEQUICKBROWNFOX
# is rewritten as

# T___U___B___N___
# _H_Q_I_K_R_W_F_X
# __E___C___O___O.

# Then it is read as TUBNHQIKRWFXECOO 


def railfence(text,key,decode=False):
    if decode == False:
        # start on rail 0
        rail = 0
        # move along the rails
        inc = 1
        fence = ["" for i in range(key)]
        for pos,let in enumerate(text):
            fence[rail] += let
            # move to the next rail
            rail += inc
            # if we have reached rail 0 or rail key-1 reverse the direction
            # that we move on the rails
            if rail == 0 or rail == key-1:
                inc *= -1

        return "".join(fence)
    
    if decode == True:
        # To decode we rebuild the fence
        
        # First how many letters are on each rail?
        chunks = [0 for i in range(key)]
        rail = 0
        inc = 1
        for pos in text:
            chunks[rail] += 1
            rail += inc
            if rail == 0 or rail == key-1:
                inc *= -1

        # Now rebuild each rail
        fence = ["" for i in range(key)]
        ctr = 0
        for pos,num in enumerate(chunks):
            fence[pos] = text[ctr:ctr+num]
            ctr += num
            
        # Finally read up and down the rails
        rail = 0
        inc = 1
        out = []
        for pos,let in enumerate(text):
            a,fence[rail] = fence[rail][0],fence[rail][1:]
            out.append(a)
            rail += inc
            if rail == 0 or rail == key-1:
                inc *= -1
                
        return "".join(out)

# A route cipher works simply by writing down the message and then reading it
# off in some unusual order.  There are a tremendous number of possible route
# route ciphers this one is very simple. The text is written left to right into
# a certain number of columns then reading up and down the columns like a
# snake.
        
# THEQUIC
# KBROWNF
# OXJUMPS
# OVERTHE
# LAZYDOG

# TKOOL AVXBH ERJAZ YRUOQ UWMTD OHPNI CFSEG
        
def routeCipher(text,key,decode=False):
    while len(text) % key != 0:
        text += "X"
    
    if decode == False:
        G = groups(text,key)
        out = ""
        ctr = 0
        while ctr < key:
            gr = []
            for i in G:
                gr.append(i[ctr])
            if ctr % 2 == 1:
                gr.reverse()
            out += "".join(gr)
            ctr += 1
    
        return out
    
    if decode == True:
        
        key = len(text)//key
        
        G = groups(text,key)
        
        out = ""
        
        for passthru in range(key):
            for pos,lets in enumerate(G):

                if pos % 2 == 0:
                    a = lets[0]
                    G[pos] = lets[1:]

                if pos % 2 == 1:
                    a = lets[-1]
                    G[pos] = lets[:-1]

                out += a

        return out
    
# The turning grille was invented by Edouard Fleissner. This version uses a
# fixed 8x8 grid.

import numpy as np

def turningGrille(text,key,decode=False,printkey=False,printgrid=False):
    
    # Can't work with more than 64 characters at a time 
    if len(text) > 64:
        raise Exception("Text is too long.")
    
    # If we have less than 64 characters first insert Xs as nulls to indicate
    # that we have reached the end of the message. Then put in common letters
    # to make the less less obvious.
    ctr = 0
    while len(text) < 64:

        if ctr > 3:
            text += choice([i for i in "ETAOINSRH"])
        else:
            text += "X"
            ctr += 1
    
    # The grille is actual key used for encryption, the key argument provided
    # specifies how to put it together.
    grille = np.zeros([8,8],dtype=int)
    # This matrix is what we will write the results into
    outmat = np.full([8,8],"")
    
    # Generate the grille to be used as the key
    for block in key:
        for digit in block:
            pos = np.divmod(digit,4)
            grille[pos[0],pos[1]] = 1
        grille = np.rot90(grille)
    
    # If requested print out the grille in a more human readable way
    if printkey == True:
        for i in grille:
            t = ["#" if j == 0 else "_" for j in i]
            print("|","|".join(t),"|",sep="")
    
    # When encoding write the letters of the text into the open spaces of the
    # grille. Then rotate the grille 90 degrees and continue.
    if decode == False:
        for rot in range(4):
            X = np.where(grille == 1)
            for i,j in zip(X[0],X[1]):
                a,text = text[0],text[1:]
                outmat[i,j] = a
            grille = np.rot90(grille)
        
        out = ""
        for i in outmat:
            if printgrid == True:
                print("".join(i))
            out += "".join(i)
            
        return out

    if decode == True:
        
        gr = groups(text,8)
        out = ""
        for rot in range(4):
            X = np.where(grille == 1)
            for i,j in zip(X[0],X[1]):
                out += gr[i][j]
            grille = np.rot90(grille)
            
        return out


#def turningGrilleN()

def railfenceExample():
    print("Example of the Rail Fence Cipher\n")
    key = 5
    print("They key is {}\n".format(key))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = railfence(ptext,key)
    dtext = railfence(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

def columnarTransportExample():

    print("Columnar Transport Example")
    key = "ILIKECHICKENEGGS"
    print("The Key Is {}".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = columnarTransport(ptext,key)
    dtext = columnarTransport(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
def doubleColumnarTransportExample():

    print("Columnar Transport Example")
    keys = ["ILIKEEGGS","BLAHDIBLAHBLAH"]
    print("The Key Is {}".format(keys))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = doubleColumnarTransport(ptext,keys)
    dtext = doubleColumnarTransport(ctext,keys,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

def routeCipherExample():

    print("Route Cipher Example")
    key = 12
    print("The Key Is {}".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = routeCipher(ptext,key)
    dtext = routeCipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

def turningGrilleExample():

    print("Turning Grille Example")
    key = [[0,3,6,13],[4,5,8,15],[1,7,10,11],[2,9,12,14]]
    print("The Grille Is:")
    turningGrille("",key,printkey=True)
    
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = turningGrille(ptext,key)
    dtext = turningGrille(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

#railfenceExample()
#columnarTransportExample()
#doubleColumnarTransportExample()
#routeCipherExample()
#turningGrilleExample()
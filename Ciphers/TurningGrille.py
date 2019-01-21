import numpy as np
from numpy.random import choice
from Ciphers.UtilityFunctions import groups
import random

# The turning grille was invented by Edouard Fleissner using an 8x8 grid.
# That used a grille with four 4x4 subgrids with spaces numbered 1 through 16. 
# In each subgrid four holes were punched out, different in every subgrid.

# Letters are written in the spaces of the grille. Then the grille is rotate by
# ninety degrees and the process continues. Then rotated and written in twice
# more.

# This version allows the grille to have any width that is a multiple of four.
# If N = 1 the grille is 4x4, if N = 2 the grille is 8x8, if N = 3 the grille
# is 12x12 and so on. Regardless of size one quarter of the spaces in each
# subgrid need to be punched out.
        
# If the text has too few characters three Xs are inserted and then after that
# are random letters. Of course this should be different if the plaintext might
# actually contain three Xs in a row.
    
# The printkey argument allows the grille to be printed out with a # showing
# where the holes are.
# The printgrid agument allows the grid containing the ciphertext to be shown
# along with the ciphertext returned as a simple string. 
def turningGrille(text,key,decode=False,N=2,printkey=False,printgrid=False):
    
    
    key = groups(key,N**2)
    
    S = N*4
        
    # Can't work with more than 64 characters at a time 
    if len(text) > S**2:
        raise Exception("Text is too long.")
    
    # If we have less than 64 characters first insert Xs as nulls to indicate
    # that we have reached the end of the message. Then put in common letters
    # to make the less less obvious.
    ctr = 0
    while len(text) < S**2:

        if ctr > 3:
            text += choice([i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
        else:
            text += "X"
            ctr += 1
    
    # The grille is actual key used for encryption, the key argument provided
    # specifies how to put it together.
    grille = np.zeros([S,S],dtype=int)
    # This matrix is what we will write the results into
    outmat = np.full([S,S],"")
    
    # Generate the grille to be used as the key
    for block in key:
        for digit in block:
            pos = np.divmod(digit,S//2)
            grille[pos[0],pos[1]] = 1
        grille = np.rot90(grille)
    
    # If requested print out the grille in a more human readable way
    if printkey == True:
        for i in grille:
            t = ["_" if j == 0 else "#" for j in i]
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
        
        gr = groups(text,S)
        out = ""
        for rot in range(4):
            X = np.where(grille == 1)
            for i,j in zip(X[0],X[1]):
                out += gr[i][j]
            grille = np.rot90(grille)
            
        return out

def turningGrilleExample():

    print("Turning Grille Example")
    key = [i for i in range(16)]
    random.shuffle(key)
    print("The Grille Is:")
    turningGrille("",key,printkey=True)
    
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = turningGrille(ptext,key)
    dtext = turningGrille(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
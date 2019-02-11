from Ciphers.UtilityFunctions import groups, makeSquare, playfairPrep, squareIndex

# The Playfair cipher was designed to be a simple enough to apply rapidly in a
# battlefield setting while strong enough to resist significant cryptanalysis.

# It first creates a square of letters. The most common version uses a 5x5 
# square with the letter J replaced by I but this program offers four versions
# of the square. 

# To encrypt letters are taken two at a time and each is found in the square.
#  If they are in the same row each is replaced with the letter to their right
#  If they are in the same column each is replaced with the letter below
#  If they are in different row and different column they are replaced by the
#    letter found by keeping the same row and moving to the column other the
#    other letter.


def playfair(text,key,decode=False,mode="IJ",printkey=False):
    
    # Make sure the text will work correctly for a playfair cipher in this mode
    text = playfairPrep(text,mode=mode)

    # Derive the alphabet to be used for the key based on the mode
    sq = makeSquare(key,mode=mode)
    sqWhere = squareIndex(sq)
    
    if printkey == True:
        if mode == "EX":
            for i in range(6):
                print(" ".join(sq[i]))

        else:
            for i in range(5):
                print(" ".join(sq[i]))
    
    G = groups(text,2)

    if decode == False:
        
        if mode == "EX":
            sz = 6
        else:
            sz = 5
    
        out = ""
        
        
        for g in G:
            A = sqWhere[g[0]]
            B = sqWhere[g[1]]
            
            
            # If they share a column
            if A[0] == B[0]:
                out += sq[A[0],(A[1]+1)%sz][0]
                out += sq[B[0],(B[1]+1)%sz][0]

            # If they share a row
            elif A[1] == B[1]:
                out += sq[(A[0]+1)%sz,A[1]][0]
                out += sq[(B[0]+1)%sz,B[1]][0]

            # Otherwise
            else:
                out += sq[A[0],B[1]][0]
                out += sq[B[0],A[1]][0]


        return out
    
    
    
    if decode == True:
        if mode == "EX":
            sz = 6
        else:
            sz = 5
    
        out = ""
        
        for g in G:
            A = sqWhere[g[0]]
            B = sqWhere[g[1]]
            
            if A[0] == B[0]:
                out += sq[A[0],(A[1]-1)%sz][0]
                out += sq[B[0],(B[1]-1)%sz][0]
                
            elif A[1] == B[1]:
                out += sq[(A[0]-1)%sz,A[1]][0]
                out += sq[(B[0]-1)%sz,B[1]][0]
                
            else:
                
                out += sq[A[0],B[1]][0]
                out += sq[B[0],A[1]][0]
        
        return out
    

def playfairExample():
    print("Example of the Playfair Cipher")

    
    for i in ["IJ","CK","KQ","EX"]:
        print("\n\nIn {} mode the key is:".format(i))
        key = "PLAYFAIREXAMPLE"
        
        ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
        ctext = playfair(ptext,key,mode=i,printkey=True)
        dtext = playfair(ctext,key,decode=True,mode=i)
        print("\nPlaintext is:  {}".format(ptext))
        print("Ciphertext is: {}".format(ctext))
        print("Decodes As:    {}".format(dtext))
        
playfairExample()
from Ciphers.UtilityFunctions import uniqueRank, addNulls
from numpy import argsort


def disruptedTransposition(text,key,decode=False):
    
    
    if len(text) > len(key)**2:
        raise Exception("Grid will be too small to fit the text")
    
    # Insert nulls
    text = addNulls(text,len(key)**2)
        
    rank = uniqueRank(key)
    
    
    # Create a blank grid
    G = ["" for i in key]

    if decode == False:

        
        # Fill each row of the grid until we reach the position of that that row
        # index in the key.
        for num in range(len(rank)):
            L = rank.index(num)+1
            G[num], text = text[:L], text[L:]
        
        # Use the remaining letters to fill in the rest of the grid
        for num in range(len(rank)):
            rm = len(key) - len(G[num])
            s,text = text[:rm], text[rm:]
            G[num] += s#.lower()
            
        #print(key)
        print("".join([str(i) for i in rank]))
        for row in G:
            print(row)
        print()
        
        # Read off the grid by rows
        out = ""
        for x in argsort(rank):
            for y in range(len(key)):
                out += G[y][x]
                
        return out
    
    if decode == True:
        
        # transpose grid
        Gt = ["" for i in key]
        text = list(text)
        for x in argsort(rank):
            for y in range(len(key)):
                Gt[x] += text.pop(0)
        
        out1 = ""
        out2 = ""
        for num in range(len(rank)):
            L = rank.index(num)+1
            
            for row in range(L):
                out1 += Gt[row][num]
                
            for row in range(L,len(key)):
                out2 += Gt[row][num]
        
        
        return out1 + out2
        
        
ptext = "THEYHAVEDISCOVEREDTHATTHEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGFLEENOW"
ctext = disruptedTransposition(ptext,"BIRTHDAYS")
dtext = disruptedTransposition(ctext,"BIRTHDAYS",decode=True)
print(ptext)
print()
print(ctext)
print()
print(dtext)
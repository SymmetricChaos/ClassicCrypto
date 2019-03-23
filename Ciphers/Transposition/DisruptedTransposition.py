from Ciphers.UtilityFunctions import uniqueRank, addNulls
from numpy import argsort


def disruptedTransposition(text,key,decode=False,complete=True):
    
    
    if len(text) > len(key)**2:
        raise Exception("Grid will be too small to fit the text")
    

        
    rank = uniqueRank(key)
    
    


    if decode == False:
        
        # Create a blank grid
        G = ["" for i in key]


        # Insert nulls if using the completed cipher
        if complete == True:
            text = addNulls(text,len(key)**2)
        else:
            text = addNulls(text,len(key)**2,sep="",alphabet=" ")
        
        
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
                    
        # Read off the grid by rows
        out = ""
        for x in argsort(rank):
            for y in range(len(key)):
                out += G[y][x]
        out = out.replace(" ","")

        return out
    
    if decode == True:
        
        # We need to know what the grid looks like so we will fill it in as if
        # we were decrypting it. This is just used to get the row lengths
        # Should find a better way to do this
        G = ["" for i in key]
        text1 = text[:]
        for num in range(len(rank)):
            L = rank.index(num)+1
            G[num], text1 = text1[:L], text1[L:]
        for num in range(len(rank)):
            rm = len(key) - len(G[num])
            s,text1 = text1[:rm], text1[rm:]
            G[num] += s#.lower()
            
        rowlens = [len(r) for r in G]
        
        # Make a grid of blank spaces
        Gt = [[" " for i in key] for i in key]
        text = list(text)
        for x in argsort(rank):
            for y in range(len(key)):

                if x < rowlens[y]:
                    Gt[y][x] = text.pop(0)
        
        X = []
        for i in Gt:
            X.append("".join(i))


        out1 = ""
        out2 = ""
        for num in range(len(rank)):
            L = rank.index(num)+1
            
            out1 += X[num][:L]
                
            out2 += X[num][L:]
        
        
        return out1 + out2
        
        

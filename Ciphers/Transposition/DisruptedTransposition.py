from Ciphers.UtilityFunctions import uniqueRank


def disruptedTransposition(text,key,decode=False):
    
    if len(text) > len(key)**2:
        raise Exception("Grid will be too small to fit the text")
    
    if len(text) < len(key)**2:
        print("!")
        nulls = len(key)**2 - len(text)
        text += "X"*nulls
    
    rank = uniqueRank(key)
    
    
    print(rank)
    print()

    
    G = ["" for i in key]
    
    for num in range(len(rank)):
        L = rank.index(num)+1
        G[num], text = text[:L], text[L:]
    
    
    for num in range(len(rank)):
        rm = len(key) - len(G[num])
        s,text = text[:rm], text[rm:]
        G[num] += s#.lower()
        
    #print(key)
    for row in G:
        print(row)
    print()
    
    out = ""
    for x in range(len(key)):
        for y in range(len(key)):
            out += G[y][x]
            
    return out
    
        
ptext = "THEYHAVEDISCOVEREDTHATTHEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGFLEEIMMEDIATELY"
ctext = disruptedTransposition(ptext,"BIRTHDAYS")
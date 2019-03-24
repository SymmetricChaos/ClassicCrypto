from Ciphers.Transposition import disruptedTransposition
from Ciphers.UtilityFunctions import uniqueRank
from Examples.ExampleTemplate import example

def disruptedTranspositionExample():
    
    
    key = "BIRTHDAYS"
    ptext = "THEYHAVEDISCOVEREDTHATTHEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGFLEENOW"
    rank = uniqueRank(key)
    print("Example of Completed Disrupted Transposition\n")
    
    print("The Key is: {}".format(key))
    
    print("\nThe plaintext is\n{}".format(ptext))
    #ptext = addNulls(ptext,len(key)**2)
    print("\nWe extend it with nulls to be\n{}".format(ptext))
    print()

    G = ["" for i in key]
    
    # Here we copy some code from the cipher to make a nice graphic
    text = ptext
    for num in range(len(rank)):
        L = rank.index(num)+1
        G[num], text = text[:L], text[L:]
        
    print("The first half of the text is read into columns like this\n")
    
    print(" ".join([str(i) for i in rank]))
    for row in G:
        print(" ".join([i for i in row]))
    print()
        
    for num in range(len(rank)):
        rm = len(key) - len(G[num])
        s,text = text[:rm], text[rm:]
        G[num] += s.lower()
    
    print("\nThe remaining text then fills in the remaining spaces. Shown here in lowercase for ease of reading.\n")
    print(" ".join([str(i) for i in rank]))
    for row in G:
        print(" ".join([i for i in row]))
    print()
    
    print("Then it is read off by columns starting with the one marked zero, then one, and so on.\n")
    
    print("The completed cipher:")
    ctext, dtext = example(disruptedTransposition,ptext,key)
    print(ctext)
    
disruptedTranspositionExample()
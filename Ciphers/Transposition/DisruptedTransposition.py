from Ciphers.UtilityFunctions import uniqueRank

key = "BIRTHDAY"

rank = uniqueRank(key)
print(rank)

S = "THEYHAVEDISCOVEREDTHEQUICKBROWNFOXFLEEATONCE"


G = ["" for i in key]

for num in range(len(rank)):
    L = rank.index(num)+1
    
    G[num], S = S[:L], S[L:]


print(key)
for row in G:
    print(row)
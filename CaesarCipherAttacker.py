from TextScoring import bigramScore

def caesar(s,k,decode=False):
    s = s.upper()
    if decode == True:
        k = 26-k
    return "".join([chr((ord(i)-65+k)%26+65) for i in s])

ctext = caesar("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG",15)

bestdecode = ""
bestscore = float("-inf")
for i in range(0,26):
    
    dtext = caesar(ctext,i,decode=True)
    s = bigramScore(dtext)
    if s > bestscore:
        bestscore = s
        bestdecode = dtext

print(ctext)
print("probably translates to")
print(bestdecode)
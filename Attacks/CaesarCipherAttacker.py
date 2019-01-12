import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import Monoalphabetic as mono
from TextScoring import quadgramScore

ptext = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
ctext = mono.caesar(ptext,15)

bestkey = 0
bestdecode = ""
bestscore = float("-inf")
for i in range(0,26):
    
    dtext = mono.caesar(ctext,i,decode=True)
    s = quadgramScore(dtext)
    if s > bestscore:
        bestkey = i
        bestscore = s
        bestdecode = dtext

print("Best Key Found: {}".format(bestkey))
print("Decodes As")
print(bestdecode)
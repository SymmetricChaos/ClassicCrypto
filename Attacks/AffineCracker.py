import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.Affine import affine
from TextScoring import quadgramScore
from itertools import product

ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
ctext = affine(ptext,[7,25])

bestkey = [0,0]
bestdecode = ""
bestscore = float("-inf")
gen = product(range(0,26),[1,3,5,7,9,11,15,17,19,21,23,25])
for i in gen:
    
    dtext = affine(ctext,i,decode=True)
    s = quadgramScore(dtext)
    if s > bestscore:
        bestkey = i
        bestscore = s
        bestdecode = dtext

print("Best Key Found: {}".format(bestkey))
print("Decodes As")
print(bestdecode)
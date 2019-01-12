
import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import VigenereCipher as vig
from TextScoring import quadgramScore
import random
import math
import numpy as np


def autokeyAttack(ctext):
    for i in range(1,6):
        print("\n\n")
        k = ctext[i:]
        print(k)
        dtext = vig.vigenereAutokey(ctext[:i],k,decode=True)
        print(dtext[i:])
        
    
    
    
ptext = "THECULTIVATIONOFTHESUGARCANEISPURSUEDTOGREATEXTENTINTHEISLANDSOFTHEWESTINDIESWHEREABOUTTHREECENTURIESAGOITWASFIRSTINTRODUCEDFROMCHINAORSOMEOTHERPARTSOFTHEEASTANDWHEREITFLOURISHESWITHGREATLUXURIANCEPARTICULARLYINMOISTANDRICHGROUNDTHESEASONFORPLANTINGITCOMMENCESABOUTTHEBEGINNINGOFAUGUST"
ctext = vig.vigenereAutokey(ptext,"THIS")

autokeyAttack(ctext)
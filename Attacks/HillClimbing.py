import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers import Playfair
from TextScoring import monogramScore
import random

ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
ctext = Playfair.playfairCipher(ptext,"PLAYFAIR",mode="IJ")

def hillclimbing(ctext):
    key = [i for i in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
    
    out = Playfair.playfairCipher(ctext,"".join(key),decode=True,mode="IJ")
    
    bestscore = float("-infinity")
    bestkey = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    for i in range(10000):
        
        newKey = key[:]
        A = random.choice([i for i in range(25)])
        B = random.choice([i for i in range(25)])
        newKey[A],newKey[B] = newKey[B],newKey[A]
        
        out = Playfair.playfairCipher(ctext,"".join(newKey),decode=True,mode="IJ")
        
        score = monogramScore(out)
        
        if score > bestscore:
            key = newKey
            bestkey = newKey
            bestscore = score
        
    print("".join(bestkey))
    print(Playfair.playfairCipher(ctext,"".join(bestkey),decode=True,mode="IJ"))
    
hillclimbing(ctext)
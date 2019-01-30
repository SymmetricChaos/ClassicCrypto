from Ciphers.Caesar import caesar
from TextScoring import quadgramScore

# Breaking the Caesar cipher is trivial since there are only 26 possible keys
# that we have to check. In order to do this automatically we will score the
# text in terms of how its quadgrams look.

def caesarCracker(ctext):

    bestkey = 0
    bestdecode = ""
    bestscore = float("-inf")
    for i in range(0,26):
        
        dtext = caesar(ctext,i,decode=True)
        s = quadgramScore(dtext)
        if s > bestscore:
            bestkey = i
            bestscore = s
            bestdecode = dtext

    print("Best Key Found: {}".format(bestkey))
    print("Decodes As")
    print(bestdecode)

def caesarCrackerExample():
    
    print("""
Example of an Attack on the Caesar Cipher

Since there are only 26 keys we will check each of them in turn and get the one
that decodes to look the most like English text. It is finding English text 
that is the only tricky part.
""")
    
    ptext = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
    ctext = caesar(ptext,15)
    
    print("\nThe ciphertext is:",ctext,"\n")
    
    caesarCracker(ctext)
    
#caesarCrackerExample()
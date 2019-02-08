from Ciphers.Affine import affine
from TextScoring import quadgramScore
from itertools import product

def affineCracker(text):
    bestkey = [0,0]
    bestdecode = ""
    bestscore = float("-inf")
    gen = product([1,3,5,7,9,11,15,17,19,21,23,25],range(0,26))
    for i in gen:
        
        dtext = affine(text,i,decode=True)
        s = quadgramScore(dtext)
        if s > bestscore:
            bestkey = i
            bestscore = s
            bestdecode = dtext
    
    print("Best Key Found: {}".format(bestkey))
    print("Decodes As:")
    print(bestdecode)

def affineCrackerExample():

    print("""
An example of an attack on the affine cipher.

Because the key space is so small we will do this by brute force. That means
simply checking each of the 312 possible keys.
""")

    ctext = "SWXPJMSNAHSNLULOSWXBJFHKPHUXNBCJKBJXGSLFKXHSXISXUSNUSWXNBMHUGBLOSWXRXBSNUGNXBRWXKXHYLJSSWKXXPXUSJKNXBHFLNSRHBONKBSNUSKLGJPXGOKLDPWNUHLKBLDXLSWXKCHKSBLOSWXXHBSHUGRWXKXNSOMLJKNBWXBRNSWFKXHSMJIJKNHUPXCHKSNPJMHKMZNUDLNBSHUGKNPWFKLJUGSWXBXHBLUOLKCMHUSNUFNSPLDDXUPXBHYLJSSWXYXFNUUNUFLOHJFJBS"
    
    affineCracker(ctext)
    
#affineCrackerExample()
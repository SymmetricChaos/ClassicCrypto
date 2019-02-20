from Ciphers.UtilityFunctions import alphabetPermutation

# The various quagmire ciphers are a variations on the vigenere cipher that use
# scrambled alphabets rather than simply shifted alphabets.


# The Quagmire One is essentially a simple substitution cipher which then has
# vigenre cipher applied on top of it.
def quagmire1(text,keys,decode=False):
    
    key = alphabetPermutation(keys[0])
    indicator = keys[1]
    
    table = []
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for lt in indicator:
        sh = (alpha.index(lt) - key.index("A")) % 26
        table.append(alpha[sh:] + alpha[:sh])
        
    out = []
    if decode == False:
        for ctr, ltr in enumerate(text):
            t = table[ctr % len(indicator)]
            out.append( t[key.index(ltr)] )
            
    if decode == True:
        for ctr, ltr in enumerate(text):
            t = table[ctr % len(indicator)]
            out.append( key[t.index(ltr)] )
    
    return "".join(out)

# The Quagmire Two applies the vigenere cipher except that rather than shifting
# the normal alphabet in accordance with the key it shifts a scrambled alphabet
# instead.
def quagmire2(text,keys,decode=False):
    key = alphabetPermutation(keys[0])
    indicator = keys[1]
    
    table = []
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for lt in indicator:
        sh = key.index(lt) % 26
        table.append(key[sh:] + key[:sh])
    
    
    out = []
    
    if decode == False:
        for ctr, ltr in enumerate(text):
            t = table[ctr % len(indicator)]
            out.append( t[alpha.index(ltr)] )
        
        return "".join(out)
    
    if decode == True:
        for ctr, ltr in enumerate(text):
            t = table[ctr % len(indicator)]
            out.append( alpha[t.index(ltr)] )
        
    return "".join(out)

# The Quagmire Three is similar to the Quagmire Two but with the first key used
# to apply a simple substitution cipher to the text first.
def quagmire3(text,keys,decode=False):
    key = alphabetPermutation(keys[0])
    indicator = keys[1]
    
    table = []
    
    for lt in indicator:
        sh = key.index(lt) % 26
        table.append(key[sh:] + key[:sh])
    
    
    
    out = []
    if decode == False:
        for ctr, ltr in enumerate(text):
            t = table[ctr % len(indicator)]
            out.append( t[key.index(ltr)] )
            
    if decode == True:
        for ctr, ltr in enumerate(text):
            t = table[ctr % len(indicator)]
            out.append( key[t.index(ltr)] )
    
    return "".join(out) 
        
# The Quagmire Four is the same as the Quagmire Three except that a different
# key is used for the intitial substitution.
def quagmire4(text,keys,decode=False):
    key1 = alphabetPermutation(keys[0])
    key2 = alphabetPermutation(keys[1])
    indicator = keys[2]
    
    table = []
    
    for lt in indicator:
        sh = key2.index(lt) % 26
        table.append(key2[sh:] + key2[:sh])
        
        
    out = []
    if decode == False:
        for ctr, ltr in enumerate(text):
            t = table[ctr % len(indicator)]
            out.append( t[key1.index(ltr)] )
    
    if decode == True:
        for ctr, ltr in enumerate(text):
            t = table[ctr % len(indicator)]
            out.append( key1[t.index(ltr)] )
    
    return "".join(out) 
        
def quagmireExample():
    print("Quagmire Examples\n")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    
    for cipher in [quagmire1,quagmire2,quagmire3]:
        
        print(cipher.__name__)
        
        key = ["ROMANCE","KINGDOMS"]
        print("The Key Is: {}".format(key))
        ctext = cipher(ptext,key)
        
        print("Plaintext is:\n{}".format(ptext))
        print("Ciphertext is:\n{}\n".format(ctext))

    
    
    key = ["SENSORY","PERCEPTION","EXTRA"]
    ctext = quagmire4(ptext,key)
    
    print("quagmire4")
    print("The Key Is: {}".format(key))
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}\n".format(ctext))
    
#quagmireExample()
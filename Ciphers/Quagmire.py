from Ciphers.UtilityFunctions import alphabetPermutation

def quagmire1(text,keys,decode=False):
    
    key = alphabetPermutation(keys[0])
    indicator = keys[1]
    
    table = []
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for lt in indicator:
        sh = (alpha.index(lt) - key.index("A")) % 26
        table.append(alpha[sh:] + alpha[:sh])
        
    out = []
    for ctr, ltr in enumerate(text):
        t = table[ctr % len(indicator)]
        out.append( t[key.index(ltr)] )
    
    return "".join(out)

def quagmire2(text,keys,decode=False):
    key = alphabetPermutation(keys[0])
    indicator = keys[1]
    
    table = []
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for lt in indicator:
        sh = key.index(lt) % 26
        table.append(key[sh:] + key[:sh])
        
    out = []
    for ctr, ltr in enumerate(text):
        t = table[ctr % len(indicator)]
        out.append( t[alpha.index(ltr)] )
    
    return "".join(out) 
        
    print(table)
    
def quagmire3(text,keys,decode=False):
    key = alphabetPermutation(keys[0])
    indicator = keys[1]
    
    table = []
    
    for lt in indicator:
        sh = key.index(lt) % 26
        table.append(key[sh:] + key[:sh])
        
    out = []
    for ctr, ltr in enumerate(text):
        t = table[ctr % len(indicator)]
        out.append( t[key.index(ltr)] )
    
    return "".join(out) 
        
    print(table)
    
def quagmire4(text,keys,decode=False):
    key1 = alphabetPermutation(keys[0])
    key2 = alphabetPermutation(keys[1])
    indicator = keys[2]
    
    table = []
    
    for lt in indicator:
        sh = key2.index(lt) % 26
        table.append(key2[sh:] + key2[:sh])
        
        
    out = []
    for ctr, ltr in enumerate(text):
        t = table[ctr % len(indicator)]
        out.append( t[key1.index(ltr)] )
    
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

    
    print("quagmire4")
    print("Plaintext is:\n{}".format(ptext))
    key = ["SENSORY","PERCEPTION","EXTRA"]
    print("The Key Is: {}".format(key))
    print(quagmire4(ptext,key))
    
#quagmireExample()
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
    pass



print(quagmire1("THEQUAGONEISAPERIODICCIPHERWITHAKEYEDPLAINALPHABET",["SPRINGFEVER","FLOWER"]))

from Ciphers.UtilityFunctions import alphabetPermutation

def quagmire1(text,keys,decode=False):
    
    key = alphabetPermutation(keys[0])
    indicator = keys[1]
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for lt in indicator:
        print(alpha.index(lt))
    
    print(key)
    print(key.index("A"))
    
quagmire1("",["SPRINGFEVER","FLOWER"])

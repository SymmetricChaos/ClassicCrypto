from Ciphers.RotorMachine import SIGABA

def SIGABAExample():

    cipher =     ["V","IX","II","IV","III"]
    control =    ["IX","VI","I","VII","VIII"]
    index =      ["II","I","V","IV","III"]
    indicator =  "TABLE"
    controlPos = "GRAPH"
    indexPos =   "02367"
    
    ptext = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG"
    
    ctext = SIGABA(ptext,[cipher,control,index,indicator,controlPos,indexPos],
                   decode=False)
    dtext = SIGABA(ctext,[cipher,control,index,indicator,controlPos,indexPos],
                   decode=True)
        
    print(ptext)
    print(ctext)
    print(dtext)
    
SIGABAExample()
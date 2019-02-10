from Ciphers.UtilityFunctions import groups, baseConvert, str2dec

# Using the ASCII 1967 standard.
def ASCII(text, decode = False, mode = "BIN"):
    
    # We use Python's triple quotes so that its possible to include " and '
    chars = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    
    modes = {"BIN": [2,7],
             "OCT": [8,3],
             "DEC": [10,3],
             "HEX": [16,2]}
    
    base, length = modes[mode]
    
    out = []
    
    # Convert to a number then convert that number to a binary string
    if decode == False:
        for let in text:
            if let not in chars:
                raise Exception("{} is not part of the ASCII67 standard")
            
            t = baseConvert(chars.index(let)+32,base)
            while len(t) < length:
                t = "0" + t
            
            out.append(t)
    
    
    if decode == True:
        for block in groups(text,length):
            n = str2dec(block,base)
            out.append(chars[n-32])

    return "".join(out)

def ASCIIExample():

    
    ptext = "The Qu1ck Brown (Fox)\Jumps 0ver the Lazy Dog!?"
    print(ptext,end="\n\n")
    
    for mode in ["BIN","OCT","DEC","HEX"]:
    
        ctext = ASCII(ptext,mode=mode)
        dtext = ASCII(ctext,decode=True,mode=mode)
        
        print(ctext)
        if dtext != ptext:
            print("DECODE ERROR")
        print()
        
ASCIIExample()
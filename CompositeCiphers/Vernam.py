from Ciphers.UtilityFunctions import saveFormat,restoreFormat
from Codes import morseCode
from RNG import LFSR




def vernam(text,key,decode=False):
    
    text, pos, char, case = saveFormat(text,"01")
    
    
    bits = LFSR(key[0],key[1],16,bits=True)
    
    out = []
    for t,b in zip(text,bits):
        if t == " ":
            out.append(" ")
            continue
        if b == 0:
            out.append(t)
        else:
            if t == "0":
                out.append("1")
            else:
                out.append("0")
    
    ftext = restoreFormat("".join(out),pos, char, case)
    
    return ftext

ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"    
ptext = morseCode(ptext,style="digit")

ctext = vernam(ptext,[6545,[15,7,4,3]])

dtext = vernam(ctext,[6545,[15,7,4,3]])

print(morseCode(ptext,decode=True,style="digit"))
print(ctext)
print(morseCode(dtext,decode=True,style="digit"))
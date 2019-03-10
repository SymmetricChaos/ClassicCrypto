from Codes import morseCode
from RNG import LFSR

ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"

print(ptext,"\n")

ctext = morseCode(ptext)
ctext = ctext.replace(" ","")
ctext = ctext.replace("-","1")
ctext = ctext.replace(".","0")
print(ctext,"\n")

bits = LFSR(156,[9,4],10,bits=True)

out = []
for c,b in zip(ctext,bits):
    if b == 0:
        out.append(c)
    else:
        if c == "0":
            out.append("1")
        else:
            out.append("0")

print(ctext)
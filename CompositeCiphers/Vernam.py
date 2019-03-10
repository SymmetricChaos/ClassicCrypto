from Ciphers.UtilityFunctions import saveFormat,restoreFormat
from Codes import morseCode
from RNG import LFSR

ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"

print(ptext,"\n")

ctext = morseCode(ptext)
ctext = ctext.replace("-","1")
ctext = ctext.replace(".","0")
print(ctext,"\n")

ctext, pos, char, case = saveFormat(ctext,"01")


bits = LFSR(156,[9,4],10,bits=True)

out = []
for c,b in zip(ctext,bits):
    if c == " ":
        out.append(" ")
        continue
    if b == 0:
        out.append(c)
    else:
        if c == "0":
            out.append("1")
        else:
            out.append("0")

ftext = restoreFormat("".join(out),pos, char, case)
print(ftext)
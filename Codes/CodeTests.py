from MorseCode import morseCode
from BaconCode import baconCode
from PrefixCode import prefixCode

def codetest(text,fun):
    ctext = fun(text)
    dtext = fun(ctext,decode=True)
    if text == dtext[:len(text)]:
        print("Success")
    else:
        raise Exception("Decode Error With {}".format(fun.__name__))


ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"

codetest(ptext,morseCode)
codetest(ptext,baconCode)
codetest(ptext,prefixCode)
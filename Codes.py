# Morse code is a very popular method of encoding letters and numbers
# variations exist for languages other than English.

def morseCode(text,decode=False):
    if "." in text or "-" in text:
        if decode == False:
            raise Exception('text contains dots and dashes')
    
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    M = [".- ","-... ","-.-. ","-.. ",". ","..-. ","--. ",".... ",
         ".. ",".--- ","-.- ",".-.. ","-- ","-. ","--- ",".--. ",
         "--.- ",".-. ","... ","- ","..- ","...- ",".-- ","-..- ",
         "-.-- ","--.. ","----- ",".---- ","..--- ","...-- ",
         "....- ","..... ","-.... ","--... ","---.. ","----. "]

    D = {}
    
    if decode == False:
        for a,m in zip(A,M):
            D[a] = m
        
        out = [D[letter] for letter in text]
        
        return "".join(out)
            
        
    if decode == True:
        for a,m in zip(A,M):
            D[m] = a
        
        text = text.split(" ")
        
        # If there are any trailing spaces remove them
        while text[-1] == " " or text[-1] == "":
            text.pop()

        out = [D[code+" "] for code in text]
        
        return "".join(out)

    
ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
ctext = morseCode(ptext)
dtext = morseCode(ctext,decode=True)
print(ctext)
print(dtext)
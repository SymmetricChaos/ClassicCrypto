# Ordinary Morse code is not a true binary code as it requires spaces in order
# to be uniquely decodeable. This means that Morse code presented without spaces
# is ambigious. Here we will use a depth first search to reveal the possible
# interpretations of an ambiguous code.

from Codes import morseCode

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
M = [".-","-...","-.-.","-..",".","..-.","--.","....",
     "..",".---","-.-",".-..","--","-.","---",".--.",
     "--.-",".-.","...","-","..-","...-",".--","-..-",
     "-.--","--..","-----",".----","..---","...--",
     "....-",".....","-....","--...","---..","----."]



def depthsearch(R,L,crib):
        
    if "EEE" in R or "TTT" in R:
        return 0
    
    if len(L) == 0:
        if crib in R:
            print(R)
        
    else:
        L = L.copy()
        cur = ""
        for i in range(min(5,len(L))):
            cur += L.pop(0)
            if cur in M:
                depthsearch(R + A[M.index(cur)],L,crib)


# A wrapper function to make it easier to use
def morseDecoder(text,crib):
    depthsearch("",list(text),crib)


for i in ["THE","AND","FOR","BUT"]:
    print(i,morseCode(i,style="block").replace("  "," "))

#ptext = morseCode("THEQUICKFOX")
#ptext = ptext.replace(" ","")
#morseDecoder(ptext,"")
#print(ptext)
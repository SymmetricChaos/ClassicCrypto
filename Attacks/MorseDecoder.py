# Ordinary Morse code is not a true binary code as it requires spaces in order
# to be uniquely decodeable. This means that Morse code presented without spaces
# is ambigious. Here we will use a depth first search to reveal the possible
# interpretations of an ambiguous code.

from Codes import morseCode
from Attacks.TextScoring import bigramScore

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
M = [".-","-...","-.-.","-..",".","..-.","--.","....",
     "..",".---","-.-",".-..","--","-.","---",".--.",
     "--.-",".-.","...","-","..-","...-",".--","-..-",
     "-.--","--..","-----",".----","..---","...--",
     "....-",".....","-....","--...","---..","----."]




# A wrapper function to make it easier to use
def morseDecoder(text,crib):
    
    
    #if morseCode(crib) not in text:
    #    raise Exception("The crib {} does not appear in the text".format(crib))
    
    out = [float("-inf"),""]
    
    def depthsearch(R,L,crib):
        
        # These strings don't occur in English text but will often appear when
        # trying to guess Morse code because both of them require only one
        # symbol to encode. Thus if we find them end the branch of recursion by
        # returning a value
        if "EEE" in R or "TTT" in R:
            return 0
        
        # If we have exhausted the symbols then check for the crib and check the
        # normalized score for the text. If that score is better than what is
        # recorded 
        if len(L) == 0:
            if crib in R:
                scr = bigramScore(R)/len(R)
                if scr > out[0]:
                    out[1] = R
                    out[0] = scr
                    print(R)
            
        else:
            L = L.copy()
            cur = ""
            for i in range(min(4,len(L))):
                cur += L.pop(0)
                if cur in M:
                    depthsearch(R + A[M.index(cur)],L,crib)

    
    depthsearch("",list(text),crib)
    
    return out[1]

ptext = morseCode("HELLO")
ptext = ptext.replace(" ","")
print(ptext)
morseDecoder(ptext,"LL")

from UtilityFunctions import alphabetPermutation

# The general substitution cipher. It simple replaces letters
# with other letters. To make this easier the key may be any sequence of
# letters from the English alphabet. The letter A is turned into to the first
# letter of the word, the letter B is turned into the second letter of the
# word and so on. If the word repeats letters those repetitions are skipped.

def substitution(text,key,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    
    # Derive the internally used key from the input
    KEY = alphabetPermutation(key)
            
    if decode == False:
        for i in text:
            out.append(KEY[alpha.index(i)])
    if decode == True:
        for i in text:
            out.append(alpha[KEY.index(i)])
    
    return "".join(out)


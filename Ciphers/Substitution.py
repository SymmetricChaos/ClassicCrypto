from Ciphers.UtilityFunctions import alphabetPermutation

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

# The atbash cipher is similar to ROT13. It is not a true cipher since the key
# is the same every time. It is also involutive as there is no difference
# encryption and decrpytion.
def atbash(text,key=None,decode=False):
    return substitution(text,"ZYXWVUTSRQPONMLKJIHGFEDCBA")

def substitutionExample():
    print("Example of a Simple Substitution Cipher\n")
    key = "ILOVEZEBRAS"
    print("The key is {}\n".format(key))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = substitution(ptext,key)
    dtext = substitution(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
def atbashExample():
    print("Example of Atbash\n")

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = atbash(ptext)
    dtext = atbash(ctext)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#substitutionExample()
#atbashExample()
from Ciphers.UtilityFunctions import alphabetPermutation, validptext, validkeys

# The general substitution cipher. It simple replaces letters
# with other letters. To make this easier the key may be any sequence of
# letters from the English alphabet. The letter A is turned into to the first
# letter of the word, the letter B is turned into the second letter of the
# word and so on. If the word repeats letters those repetitions are skipped.

def substitution(text,key,decode=False,alphabet=""):
    
    if alphabet == "":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    validptext(text,alphabet)
    validkeys(key,str)
    
    # Derive the internally used key from the input
    KEY = alphabetPermutation(key,alphabet)
    
    out = []
    if decode == False:
        for i in text:
            out.append(KEY[alphabet.index(i)])
    if decode == True:
        for i in text:
            out.append(alphabet[KEY.index(i)])
    
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
    
    
    print("\n\nExample of a Custom Alphabet")
    key = "0I1L2O3V4E5Z6E7B8R9AS"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    print("Alphabet: {}".format(alpha))
    print("Key: {}\n".format(key))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = substitution(ptext,key,alphabet=alpha)
    dtext = substitution(ctext,key,decode=True,alphabet=alpha)
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
    
substitutionExample()
#atbashExample()
from CompositeCipher import compositeCipher
import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.Vigenere import vigenere
from Ciphers.ColumnarTransport import columnarTransport
from Ciphers.DRYAD import DRYAD
from Ciphers.StraddlingCheckerboard import straddlingCheckerboard
from Ciphers.HillCipher import hillCipher
from Ciphers.Substitution import substitution

def Checkerboard_DRYAD(text,keys,decode=False):
    return compositeCipher(text,[straddlingCheckerboard,DRYAD],keys,decode=decode)


# A simple but very strong combination of ciphers
def Vigenere_Columnar(text,keys,decode=False):
    return compositeCipher(text,[vigenere,columnarTransport],keys,decode=decode)


# The Hill cipher presented in the Ciphers section is not an especially secure
# form of encryption because it is completely linear and the key can be found
# if a few strings of text from the original text. Hill suggested that this can
# be corrected by applying a simple substitution cipher.
def Hill_Substiution(text,keys,decode=False):
    return compositeCipher(text,[hillCipher,substitution],keys,decode=decode)


def Checkerboard_DRYAD_Example():
    print("Example of the Checkerboard Dryad Cipher\n")
    key = [["ZEBRA",[1,3]],7656751]
    print("They key is {}\n".format(key))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = Checkerboard_DRYAD(ptext,key)
    dtext = Checkerboard_DRYAD(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))

def Vigenere_Columnar_Example():
    print("Example of the Vigenere Columnar Cipher\n")
    key = ["APPLE","CIPHERS"]
    print("They key is {}\n".format(key))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = Vigenere_Columnar(ptext,key)
    dtext = Vigenere_Columnar(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
def Hill_Substiution_Example():
    print("Example of the Hill Substiution Cipher\n")
    key = ["APPLE","CIPHERS"]
    print("They key is {}\n".format(key))
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = Hill_Substiution(ptext,key)
    dtext = Hill_Substiution(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
    
Checkerboard_DRYAD_Example()
print("\n\n")
Vigenere_Columnar_Example()
print("\n\n")
Hill_Substiution_Example()
from CompositeCipher import compositeCipher
import sys
sys.path.append("C:\\Users\\Alexander\\Documents\\GitHub\\ClassicCrypto")
from Ciphers.Vigenere import vigenere
from Ciphers.ColumnarTransport import columnarTransport
from Ciphers.DRYAD import DRYAD
from Ciphers.StraddlingCheckerboard import straddlingCheckerboard

def Checkerboard_DRYAD(text,keys,decode=False):
    return compositeCipher(text,[straddlingCheckerboard,DRYAD],keys,decode=decode)

def Vigenere_Columnar(text,keys,decode=False):
    return compositeCipher(text,[vigenere,columnarTransport],keys,decode=decode)

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
    

Checkerboard_DRYAD_Example()
print("\n\n")
Vigenere_Columnar_Example()

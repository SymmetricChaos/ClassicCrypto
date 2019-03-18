from Ciphers import straddlingCheckerboard
from Ciphers.UtilityFunctions import alphabetPermutation

def showCheckerboard(keys):
    al = list(alphabetPermutation(keys[0]))
    
    print("  0 1 2 3 4 5 6 7 8 9")
    print("  ",end="")
    for i in range(10):
        if i not in keys[1]:
            print(al.pop(0),end=" ")
        else:
            print(" ",end=" ")
            
    print("\n{} ".format(keys[1][0]),end="")
    
    for i in range(10):
        print(al.pop(0),end=" ")
    
    print("\n{} ".format(keys[1][1]),end="")
    for i in range(8):
        print(al.pop(0),end=" ")
    print("\n")

def straddlingCheckerboardExample():
    print("Example of the Straddling Checkerboard\n")
    keys = ["ZEBRA",[1,3]]
    print("The key is {}\n".format(keys))
    
    showCheckerboard(keys)
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = straddlingCheckerboard(ptext,keys)
    dtext = straddlingCheckerboard(ctext,keys,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    
#straddlingCheckerboardExample()
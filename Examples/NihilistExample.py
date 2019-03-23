from Ciphers import nihilist
from Examples.ExampleTemplate import example

def nihilistExample():
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    key = ["SOMETHING","NIHILIST"]
    print("Example Of The Nihilist Cipher\n\nKey is {}\n".format(key))

    c, d = example(nihilist,ptext,key)
    print(c)
    
nihilistExample()
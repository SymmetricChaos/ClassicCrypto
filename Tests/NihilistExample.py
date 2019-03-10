from Ciphers import nihilist
from Tests.ExampleTemplate import example

def nihilistExample():
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    key = ["SOMETHING","NIHILIST"]
    print("Example Of The Nihilist Cipher\n\nKey is {}\n".format(key))

    example(nihilist,ptext,key)
    
nihilistExample()
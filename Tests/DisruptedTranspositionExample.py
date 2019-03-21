from Ciphers import disruptedTransposition

def disruptedTranspositionExample()

    ptext = "THEYHAVEDISCOVEREDTHATTHEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGFLEENOW"
    ctext = disruptedTransposition(ptext,"BIRTHDAYS")
    dtext = disruptedTransposition(ctext,"BIRTHDAYS",decode=True)
    print(ptext)
    print()
    print(ctext)
    print()
    print(dtext)
from Ciphers.RotorMachine import enigma
import random
from Ciphers.UtilityFunctions import groups
import datetime

def enigmaExample():
        
    print("Enigma Example\n")
    
    # The Enigma machine had a codebook with different settings to be used
    # each day. This example just uses a hash of the date to randomly pick
    # what the settings will be. In actual use a stronger form of randomness is
    # needed.
    today = datetime.datetime.now().date()
    print("Today is {}\nThe Codebook Settings Are:".format(today))
    random.seed(hash(today))
    
    # Randomly pick the rotors, the reflector, the positions, and the plugboard
    # settings for the day
    rotors = random.sample(["I","II","III","IV","V"],k=3)
    reflector = random.choice(["A","B","C"])
    positions = random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=3)
    plugs = []
    for i in groups(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=20),2):
        plugs.append("".join(i))

    # Write out those settings separated by a | symbol
    print(reflector,end = " | ")
    for i in rotors:
        print(i,end = " ")
    print("| ",end = "")
    for i in positions:
        print(i,end = "")
    print(" | ",end = "")
    for i in plugs:
        print(i,end = " ")
        
    # Whenever an Enigma message was sent it was preceeded by the ring settings
    # which told the recieving operator what offset from the day's rotor
    # positions should be used. This meant that a different cipher could be
    # used for every message without revealing exactly what the settnings were.
    rings = ["A","B","C"]
    print("\n\nRing Settings:",end= " ")
    for i in rings:
        print(i,end = " ")
    print("\n")
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOGANDJACKDAWSLOVEMYBIGSPHINXOFQUARTZ"
    ctext = enigma(ptext,keys=[rotors,reflector,positions,plugs,rings])
    dtext = enigma(ctext,keys=[rotors,reflector,positions,plugs,rings])
    print(ctext)
    if dtext != ptext:
        print("ERROR")
        print(dtext)

enigmaExample()
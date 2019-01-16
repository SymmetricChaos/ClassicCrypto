# An Engima style rotor machine. The method is actually quite simple. Each
# letter is encrypted by a series of simple substitution ciphers that change
# automatically for each letter. However because this behavior is quite regular
# it is not especially hard to break the resulting cipher. Using the plugboard
# to swap letters makes it significantly more secure. The military Enigma
# historically chose ten letter pairs.

# Because this simulated rotor machine can accept arbitrary rotors even if the
# number of rotors in use is known the key space is absurdly large. However
# rotor machines like this are very well analyzed and should not be considered
# secure simply because of the number of possible keys.

# This is NOT a simulation of the actual Enigma machine as that included a
# some mechanisms this does not such as rotors that stepped at two different
# places.

# Pass a singal through a rotor
def rotor(letter,key,decode=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if decode == False:
        return key[alpha.index(letter)]
    if decode == True:
        return alpha[key.index(letter)]

# Step a rotor forward by one
def step(R):
    return R[1:] + R[0]

# The plugboard (Steckerbrett) flips pairs of letters
# Pairs of letters are not allowed to overlap
def plugboard(text,keys):
    
    if keys == []:
        return text
    
    # A very messy bit of code that makes sure only unique pairs of letters
    # are swapped.
    for pos,key in enumerate(keys):
        for let in key:
            for i in range(pos+1,len(keys)):
                if let in keys[i]:
                    raise Exception('pairs of letters cannot overlap')
    
    # Do the swapping
    for key in keys:
        text = text.replace(key[0],"*")
        text = text.replace(key[1],key[0])
        text = text.replace("*",key[1])
    return text

# Implement the rotor machine itself
def rotorMachine(text,keys,decode=False):
    
    if len(keys) != 3:
        raise Exception('the "keys" argument must provide rotors, notches, and plug settings\nfor an empty plugboard use []')
    
    # The rotor list will be changed while the machine is in operation to
    # prevent this from causing issues we will use a copy of the list instead
    rotors = keys[0][:]
    notches = keys[1]
    plugs = keys[2]
    
    # Make sure that every rotor has a notch
    if len(rotors) != len(notches):
        raise Exception('there must be an equal number of rotors and notch positions')
    
    # Make sure that every rotor is correct
    for pos,rtr in enumerate(rotors):
        if "".join(sorted(rtr)) != "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            raise Exception('rotor {} is invalid'.format(pos+1))
    
    
    text = plugboard(text,plugs)
    

    out = []
    

    # For each letter
    for letter in text:
        #Pass that letter through the rotors
        t = letter
        for r in rotors:
            t = rotor(t,r,decode=decode)
        
        # The last rotors is assumed to be the reflector
        # Now go through the other rotors in reverse 
        for r in rotors[1::-1]:
            t = rotor(t,r,decode=decode)
        

        # Save the result
        out.append(t)
        
        # Step the rotors forward.
        rotors[0] = step(rotors[0])
        for n in range(len(notches)-1):
            if rotors[n][0] == notches[n]:
                rotors[n+1] = step(rotors[n+1])

    out = "".join(out)

    return plugboard(out,plugs)

# Should get around to a copy of Enigma at some point
def enigma(text,keys,decode=False):
    
    if len(keys) != 4:
        raise Exception('the "keys" argument must provide rotors, ring settings, reflector, and plug settings\nfor an empty plugboard use []')
    
    rtr = keys[0]
    rotors = []
    notches = []
    for num in rtr:
        if num == "I":
            rotors.append("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
            notches.append("X")
        if num == "II":
            rotors.append("AJDKSIRUXBLHWTMCQGZNPYFVOE")
            notches.append("S")
        if num == "III":
            rotors.append("BDFHJLCPRTXVZNYEIWGAKMUSQO")
            notches.append("M")
        if num == "IV":
            rotors.append("ESOVPZJAYQUIRHXLNFTGKDCMWB")
            notches.append("Q")
        if num == "V":
            rotors.append("VZBRGITYUPSDNHLXAWMJQOFECK")
            notches.append("K")


    rings = keys[1]

    reflector = ""
    if keys[2] == "RA":
        reflector = "EJMZALYXVBWFCRQUONTSPIKHGD"
    if keys[2] == "RB":
        reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    if keys[2] == "RC":
        reflector = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


    plugs = keys[3]
    
    text = plugboard(text,plugs)
    
    out = []
    
    # For each letter
    for letter in text:
        # Pass that letter through the rotors
        t = letter
        for r in rotors:
            t = rotor(t,r,decode=decode)
        
        # Now it goes through the reflector
        t = rotor(t,reflector,decode=decode)
        
        # The last rotors is assumed to be the reflector
        # Now go through the other rotors in reverse 
        for r in rotors[::-1]:
            t = rotor(t,r,decode=decode)
        
        out.append(t)
            
        # Step the rotors forward.
        rotors[0] = step(rotors[0])
        for n in range(len(notches)):
            if rotors[n][0] == notches[n]:
                rotors[n+1] = step(rotors[n+1])
    
    out = "".join(out)
    
    out = plugboard(out,plugs)
    
    print("".join(out))
    
enigma("AAAAA",keys=[["I","II","III"],[],"RB",[]])

# Should get around to a copy of SIGABA at some point
def SIGABA(text,keys,decode=False):
    pass

def rotorMachineExample():

    print("Example of a Simple Rotor Machine\n")
    
    
    R1 = "DMTWSILRUYQNKFEJCAZBPGXOHV"
    R2 = "HQZGPJTMOBLNCIFDYAWVEUSRKX"
    R3 = "UQNTLSZFMREHDPXKIBVYGJCWOA"
    
    keySettings = [[R1,R2,R3],["R","F","W"],["AB","CD","XJ","ZY"]]
    
    print("The initial rotor settings are:")
    for r in keySettings[0]:
        print(r)
    print("\nThe notches are placed at: {}".format(keySettings[1]))
    print("The plugboard pairs are: {}\n".format(keySettings[2]))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = rotorMachine(ptext,keys=keySettings)
    print()
    dtext = rotorMachine(ctext,keys=keySettings,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
    



#rotorMachineExample()
# An engima style rotor machine.

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

# Implement the rotor machine itself
def rotorMachine(text,keys,decode=False):

    rotors = keys[0]
    notches = keys[1]
    
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


    return "".join(out)

R1 = "DMTWSILRUYQNKFEJCAZBPGXOHV"
R2 = "HQZGPJTMOBLNCIFDYAWVEUSRKX"
R3 = "UQNTLSZFMREHDPXKIBVYGJCWOA"

ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
ctext = rotorMachine(ptext,keys=[[R1,R2,R3],["R","F","W"]])
dtext = rotorMachine(ctext,keys=[[R1,R2,R3],["R","F","W"]],decode=True)
print(ptext)
print(ctext)
print(dtext)
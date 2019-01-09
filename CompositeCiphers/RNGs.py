import random

# Here are a few pseudorandom number generators that are somewhat practical to
# perform with a pen and paper. While they are completely inappropriate for any
# modern cryptographic system they are useful for demonstration. All examples
# are in the form of generators.

# Weyel sequences produce numbers that are equally distributed within the range
# given by the modulus. All that is necessary is ordinary multiplication and
# then taking the modulus. If the modulus is a power of ten this can be done
# very easily by hand just dropping the higher digits.
# The seed number must be coprime to the modulus.
def Weyel(seed,mod):
    ctr = 0
    while True:
        ctr += 1
        yield (seed*ctr) % mod

# Linear Congruential generators require only multiplication adition and taking
# the modulus of a number. Choosing the parameters of an LCG has a large impact
# on the quality of the output. It is straightforward to calculate by hand and
# also not difficult with a simple machine.
def LCG(seed,mod,mult,incr):
    while True:
        seed = (mult*seed+incr) % mod
        yield seed

# The German reihenschieber was a simple sliderule system designed to create
# sequences of random digits. In actual use the sticks and grille are of course
# physical items given to people using the system.

# Utility function to make a random Reihenschieber stick
# In practice these must be distributed among users
def makeReihenschieberStick():
    alpha = ["0","1","2","3","4","5","6","7","8","9","."]
    return "".join(random.choices(alpha,k=40))

# Utility function to make a visualization of the grille used for the Reihenschieber

def showReihenschieberGrille(grille):
    G = [[0,0,0,0,0,0,0,0,0,0] for i in range(10)]
    for loc in grille:
        G[loc//10][loc%10] = 1
    for row in G:
        t = ["_" if j == 0 else "#" for j in row]
        print("|","|".join(t),"|",sep="")

# Actually implement the random number generator
def Reihenschieber(sticks,grille,stickspos,grillepos):
    
    for i in range(10):
        sticks[i] += "."*10
    

    shiftedSticks = []
    for st,p in zip(sticks,stickspos):
        covered = p+grillepos
        shiftedSticks.append(st[covered:covered+10])

    
    out = []
    for col in range(10):
        for loc in grille:
            if loc%10 == col:
                D = shiftedSticks[loc//10][loc%10]
                if D != ".":
                    out.append(int(D))
    print(out)

        
def WeyelExample():
    print("Example of the Weyel Random Number Generator\n")
    modulus = 100000
    seed = 25763
    print("Modulus is:    {}".format(modulus))
    print("Seed value is: {}\n".format(seed))
    for ctr,i in enumerate(Weyel(seed,modulus)):
        print(i)
        if ctr > 20:
            break
    print("\nNotice the periodicity of the low order bits.")
      
        
def LCGExample():
    print("Example of Linear Congruential Generator\n")
    modulus = 100000
    multiplier = 2991
    increment = 2571
    seed = 237
    print("Modulus is:    {}".format(modulus))
    print("Multiplier is: {}".format(multiplier))
    print("Increment is:  {}".format(increment))
    print("Seed value is: {}\n".format(seed))
    for ctr,i in enumerate(LCG(seed,modulus,multiplier,increment)):
        print(i)
        if ctr > 20:
            break
    print("\nNotice the periodicity of the low order bits.")
        
    
def ReihenschieberExample():
    
    print("Example of the Reihenschieber\n")
    sticks = [makeReihenschieberStick() for i in range(10)]
    grille = random.sample([i for i in range(100)],20)
    
    print("Sticks Used:")
    for s in sticks:
        print(s)
    print("\nGrille Used:")
    showReihenschieberGrille(grille)
    print()
    Reihenschieber(sticks,grille,[0,3,2,5,7,1,2,9,4,8],25)

WeyelExample()
print("\n\n")
LCGExample()
print("\n\n")
ReihenschieberExample()
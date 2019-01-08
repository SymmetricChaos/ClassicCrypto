import random

# Here are a few pseudorandom number generators that are somewhat practical to
# perform with a pen and paper. While they are completely inappropriate for any
# modern cryptographic system they are useful for demonstration. All examples
# are in the form of generators.

# Weyel sequences produce numbers that are equally distributed within the range
# given by the modulus. All that is necessary is ordinary multiplication and
# then taking the modulus. When working by hand a modulus that is a multple of
# ten is very easy.
# The seed number must be coprime to the modulus.
def Weyel(seed,mod):
    ctr = 0
    while True:
        ctr += 1
        yield (seed*ctr) % mod

# Linear Congruential generators require only multiplication adition and taking
# the modulus of a number. Choosing the parameters of an LCG has a large impact
# on the quality of the output.
def LCG(seed,mod,mult,incr):
    while True:
        seed = (mult*seed+incr) % mod
        yield seed

# The German reihenschieber was a simple sliderule system designed to create
# sequences of random digits. In actual use the sticks and grille are of course
# physical
def makeReihenschieberStick():
    alpha = ["0","1","2","3","4","5","6","7","8","9","."]
    return "".join(random.choices(alpha,k=40))

def showReihenschieberGrille(grille):
    G = [[0,0,0,0,0,0,0,0,0,0] for i in range(10)]
    for loc in grille:
        G[loc//10][loc%10] = 1
    for row in G:
        t = ["_" if j == 0 else "#" for j in row]
        print("|","|".join(t),"|",sep="")
        
def Reihenschieber(sticks,grille,stickspos,grillepos):
    
    for i in range(10):
        sticks[i] += "."*10
    
    # Create the grille? Probably a better way to do this
    G = [[0,0,0,0,0,0,0,0,0,0] for i in range(10)]
    for loc in grille:
        G[loc//10][loc%10] = 1

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
    print("Seed value is: {}".format(seed))
    for ctr,i in enumerate(Weyel(seed,modulus)):
        print(i)
        if ctr > 20:
            break
    print("Notice the periodicity of the low order bits.")
      
        
def LCGExample():
    print("Example of Linear Congruential Generator\n")
    modulus = 100000
    multiplier  = 2991
    increment = 2571
    seed = 237
    print("Modulus is:    {}".format(modulus))
    print("Multiplier is: {}".format(multiplier))
    print("Increment is:  {}".format(increment))
    print("Seed value is: {}".format(seed))
    for ctr,i in enumerate(LCG(seed,modulus,multiplier,increment)):
        print(i)
        if ctr > 20:
            break
    print("Notice the periodicity of the low order bits.")
        
    
def ReihenschieberExample():
    
    print("Example of the Reihenschieber\n")
    sticks = [makeReihenschieberStick() for i in range(10)]
    grille = [0,7,13,17,26,32,45,51,55,69,75,81,90]
    for s in sticks:
        print(s)
    print()
    showReihenschieberGrille(grille)
    Reihenschieber(sticks,grille,[0,3,2,5,7,1,2,9,4,8],25)

#WeyelExample()
#print("\n\n")
#LCGExample()
ReihenschieberExample()
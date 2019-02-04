import random
# The German reihenschieber was a simple sliderule system designed to create
# sequences of random digits. In actual use the sticks and grille are of course
# physical items given to people using the system.

# Utility function to make a random Reihenschieber stick
# In practice these must be distributed among users
def makeReihenschieberStick():
    alpha = ["0","1","2","3","4","5","6","7","8","9",".","."]
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
    
def ReihenschieberExample():
    
    print("Example of the Reihenschieber\n")
    sticks = [makeReihenschieberStick() for i in range(10)]
    grille = random.sample([i for i in range(100)],25)
    
    print("Sticks Used:")
    for s in sticks:
        print(s)
    print("\nGrille Used:")
    showReihenschieberGrille(grille)
    print()
    Reihenschieber(sticks,grille,[0,3,2,5,7,1,2,9,4,8],5)

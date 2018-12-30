# Here are a few random number generators that are somewhat practical to
# perform with a pen and paper.

# Weyel sequences 
def Weyel(seed,mod):
    ctr = 0
    while True:
        ctr += 1
        yield (seed*ctr) % mod

def LCG(seed,mod,mult,incr):
    while True:
        seed = (mult*seed+incr) % mod
        yield seed
        


#for ctr,i in enumerate(LCG(233,100000,7,81)):
#    print(i)
#    if ctr > 100:
#        break

print()
for ctr,i in enumerate(Weyel(717189,1000000)):
    print(i)
    if ctr > 50:
        break
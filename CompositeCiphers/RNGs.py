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
        


#for ctr,i in enumerate(LCG(233,100000,7,81)):
#    print(i)
#    if ctr > 100:
#        break

print()
for ctr,i in enumerate(Weyel(512785,1000000)):
    print(i)
    if ctr > 50:
        break
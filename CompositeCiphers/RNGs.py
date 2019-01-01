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
        
WeyelExample()
print("\n\n")
LCGExample()
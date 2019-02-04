# Linear Congruential generators require only multiplication adition and taking
# the modulus of a number. Choosing the parameters of an LCG has a large impact
# on the quality of the output. It is straightforward to calculate by hand and
# also not difficult with a simple machine.
def LCG(seed,mod,mult,incr):
    while True:
        seed = (mult*seed+incr) % mod
        yield seed

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
        
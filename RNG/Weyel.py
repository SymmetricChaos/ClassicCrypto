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
      
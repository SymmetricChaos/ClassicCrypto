# A linear feedback shift register is a simple form of random number generator
# that can be executed with a pen and paper without much difficulty. Very fast
# versions can be made with mechanical or electromechanical systems.

# The method is simple. A string of 0s and 1s is written out and a few positions
# are chosen as "taps". The binary string is turned into a number, then the
# taps are counted. If there are an even number of 1s in at the tap positions
# a 0 is put at the end of the list. Then the bit at the other end is removed.

#   T   T   T T
# 0 1 1 0 1 0 0 0 = 104
# 1 1 0 1 0 0 0 1 = 209
# 1 0 1 0 0 0 1 0 = 162
# 0 1 0 0 0 1 0 0 = 68
# 1 0 0 0 1 0 0 1 = 137

# These numbers are not significantly more secure than the other random number
# generators presented here. However they do appear to be more random when
# written in decimal.

# The choice of tap positions has a strong influence on how long it takes for
# the 

from Ciphers.UtilityFunctions import baseConvert, str2dec

def LFSR(seed,taps,length):
    reg = baseConvert(seed,2)
    reg = [int(i) for i in reg]

    # Put zeroes at the beginning to pad out as needed
    while len(reg) < length:
        reg.insert(0,0)
    
    # Keep returning random numbers
    while True:
        
        # Odd or even taps? (ie sum them modulo 2, ie XOR them)
        t = sum([reg[s] for s in taps]) % 2
        
        # Insert the new number at the start of the list
        reg.insert(0,t)
        
        # Remove the last element of the list
        del reg[-1]
        
        # Convert the list into a string
        S = "".join([str(i) for i in reg])
        
        # Turn the binary string back into a decimal number
        yield int(str2dec(S,2))

def LFSRExample():
    print("Example of Linear Feedback Shift Register\n")
    seed = 635
    taps = [4,6,7,15]
    length = 16
    print("Seed value is: {}".format(seed))
    print("Taps are at:   {}".format(taps))
    print("\nOutput:")
    for ctr,i in enumerate(LFSR(seed,taps,length)):
        print(i)
        if ctr > 20:
            break

    L = []
    for i in LFSR(seed,taps,length):
        if i in L:
            print()
            print("Period:",len(L))
            break
        L.append(i)

#LFSRExample()
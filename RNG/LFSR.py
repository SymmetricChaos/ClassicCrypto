# A linear feedback shift register is a simple form of random number generator
# that can be executed with a pen and paper without much difficulty. Very fast
# versions 

from Ciphers.UtilityFunctions import baseConvert, str2dec

def LFSR(seed,taps,length):
    reg = baseConvert(seed,2)
    reg = [int(i) for i in reg]

    while len(reg) < length:
        reg.append(0)
        
    while True:
        t = sum([reg[s] for s in taps]) % 2
        reg.append(t)
        del reg[0]
        
        # Convert to a string
        S = "".join([str(i) for i in reg])
        
        # Turn the binary string back into a decimal number
        yield int(str2dec(S,2))

def LFSRExample():
    print("Example of Linear Feedback Shift Register\n")
    seed = 635
    taps = [1,11,12,13]
    length = 16
    print("Seed value is: {}".format(seed))
    print("Taps are at:   {}".format(taps))
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

LFSRExample()

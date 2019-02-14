# A linear feedback shift register is a simple form of random number generator
# althought it is not simple enough to do mentally. However it can be done with
# a simple machine. Usually LFSRs are considered for binary strings but the one
# presented here use digits.

def LFSR(seed,taps):
    reg = [int(i) for i in str(seed)]

    while True:
        t = sum([reg[s] for s in taps]) % 10
        reg.append(t)
        del reg[0]
        yield int("".join([str(i) for i in reg]))

def LFSRExample():
    print("Example of Linear Feedback Shift Register\n")
    seed = 2871347615
    taps = [3,5,8]
    print("Seed value is: {}".format(seed))
    print("Taps are at:   {}".format(taps))
    for ctr,i in enumerate(LFSR(seed,taps)):
        print(i)
        if ctr > 20:
            break
    print("\nNotice the simple relationship between outputs.")

    print("\nBetter randomness can be achieved by only taking results occasionally.")
    print("Here we take every tenth output.\n")
    for ctr,i in enumerate(LFSR(seed,taps)):
        if ctr % 10 == 0:
            print(i)
        if ctr > 200:
            break
    
#LFSRExample()
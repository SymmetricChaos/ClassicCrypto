from Ciphers import straddlingCheckerboard

def VICkeystream(S):
    if len(S) != 20:
        raise Exception("Keyphrase must be 20 letters")
    

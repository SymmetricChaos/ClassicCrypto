# The rail fence cipher is a transposition cipher than writes the letters of
# plaintext up and down the rails of an imaginary fence then reads the rails
# one at a time.

# So for three rails the sentence
# THEQUICKBROWNFOX
# is rewritten as

# T___U___B___N___
# _H_Q_I_K_R_W_F_X
# __E___C___O___O.

# Then it is read as TUBNHQIKRWFXECOO 


def railfence(text,key,decode=False):
    if decode == False:
        # start on rail 0
        rail = 0
        # move along the rails
        inc = 1
        fence = ["" for i in range(key)]
        for pos,let in enumerate(text):
            fence[rail] += let
            # move to the next rail
            rail += inc
            # if we have reached rail 0 or rail key-1 reverse the direction
            # that we move on the rails
            if rail == 0 or rail == key-1:
                inc *= -1

        return "".join(fence)
    
    if decode == True:
        # To decode we rebuild the fence
        
        # First how many letters are on each rail?
        chunks = [0 for i in range(key)]
        rail = 0
        inc = 1
        for pos in text:
            chunks[rail] += 1
            rail += inc
            if rail == 0 or rail == key-1:
                inc *= -1

        # Now rebuild each rail
        fence = ["" for i in range(key)]
        ctr = 0
        for pos,num in enumerate(chunks):
            fence[pos] = text[ctr:ctr+num]
            ctr += num
            
        # Finally read up and down the rails
        rail = 0
        inc = 1
        out = []
        for pos,let in enumerate(text):
            a,fence[rail] = fence[rail][0],fence[rail][1:]
            out.append(a)
            rail += inc
            if rail == 0 or rail == key-1:
                inc *= -1
                
        return "".join(out)

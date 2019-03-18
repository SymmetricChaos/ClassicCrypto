from Ciphers.UtilityFunctions import alphabetPermutation

# The straddling checkerboard is a form of substitution cipher that converts
# each letter into a variable length commaless code in a way best understood
# by example. Like the polybius square the alphabet is placed into a grid and
# the letters are encoded as the corresponding row and column.

#    0 1 2 3 4 5 6 7 8 9
#  | A B C D   E F   G H
# 4| I J K L M N O P Q R
# 7| S T U V W X Y Z

# So in this example the phrase FLEEATONCE becomes
# 6 43 5 5 0 71 46 45 2 5
# Which can be read without spaces as
# 64355071464525
# There is no ambiguity because every two digit code MUST start with a 4 or a 7
# while NO single digit code can ever start with 4 or 7.

def straddlingCheckerboard(text,keys=["A",[0,1]],decode=False,alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):

    if len(keys) != 2:
        raise Exception('must provide both keys')
    if len(keys[1]) != 2:
        raise Exception('must provide two numbers for checkboard')
    
    # Derive the internally used key from the input
    KEY = alphabetPermutation(keys[0],alphabet)
    # Divide they KEY into a mutable list so we can pop from it
    KEY = list(KEY)
    
    D = {}
    
    if decode == False:

        # First row of the checkerboard
        for i in range(10):
            if i not in keys[1]:
                D[KEY.pop(0)] = str(i)
        
        # Second row
        for i in range(10):
            codegroup = str(keys[1][0])+str(i)
            D[KEY.pop(0)] = codegroup

        # Third row   
        for i in range(8):
            codegroup = str(keys[1][1])+str(i)
            D[KEY.pop(0)] = codegroup

        return "".join([D[letter] for letter in text])
    
    if decode == True:
        # First row of the checkerboard
        for i in range(10):
            if i not in keys[1]:
                D[str(i)] = KEY.pop(0)
        
        # Second row
        for i in range(10):
            codegroup = str(keys[1][0])+str(i)
            D[codegroup] = KEY.pop(0)

        # Third row   
        for i in range(8):
            codegroup = str(keys[1][1])+str(i)
            D[codegroup] = KEY.pop(0)
        
        L = []
        text = [sym for sym in text]

        while len(text) > 0:
            if text[0] in str(keys[1]):
                L.append(text.pop(0)+text.pop(0))
            else:
                L.append(text.pop(0))
                
        return "".join([D[i] for i in L])
    
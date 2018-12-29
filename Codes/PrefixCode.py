# A prefix code is any code in which words can be of various lengths but which
# does not need commas to show the breaks between them. There are many ways to
# accomplish this. This example uses the Fibonnaci numbers. To keep the encoded
# text as short as possible short codes are given to common letters. However it
# is still not especially compact.

# Of interest for classical cryptopgrahy is that a variable length encoding can
# disguised the actual length of the message.

# Lagged fibonnaci numbers the sequence starts: 1,2,3,5,8,11
def fibonnaci(n):
    a = 1
    b = 1
    out = []
    for i in range(n):
        out.append(a)
        a,b = a+b,a
    return out

# There has to be a better way to do this, right?
# Go through the list for the first few Fibonnaci numbers from greatest to
# make a list of Fibonnaci numbers that add up to each code number (1,2,3...)
# The code is then the indexes of those Fibonnaci numbers, with leading zeroes
# removed, reversed, with an additional "1" at the end.
def makeCodebook(decode=False):
    F = fibonnaci(10)
    F.reverse()
    codes = []
    for x in range(1,27):
        while x != 0:
            code = []
            for f in F:
                if f <= x:
                    code.append("1")
                    x = x-f
                else:
                    code.append("0")

            while code[0] == "0":

                code.pop(0)
            code.reverse()
            code.append("1")
            codes.append("".join(code))
            
    # Matchup codes with letters
    D = {}
    alpha = "ETAOINSRHLDCUMFPGWYBVKXJQZ"
    if decode == False:
        for a,b in zip(alpha,codes):
            D[a] = b
            
    if decode == True:
        for a,b in zip(alpha,codes):
            D[b] = a
    return D
    
def prefixCode(text,decode=False):
    
    # Build the codebook
    D = makeCodebook(decode=decode)
    
    # When encoding we simply translate each letter to its code
    if decode == False:
        out = []
        for letter in text:
            out.append(D[letter])
        return "".join(out)
    
    # When decoding we put the bits into a buffer one at a time until it
    # matches a code. Once it matches we record the letter and then we clear
    # the buffer.
    if decode == True:
        out = []
        bits = [b for b in text]
        code = ""
        while len(bits) > 0:
            code += bits.pop(0)[0]
            if code in list(D.keys()):
                out.append(D[code])
                code = ""
        return "".join(out)
            

ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
ctext = prefixCode(ptext)
dtext = prefixCode(ctext,decode=True)

print(ptext)
print(ctext)
print(dtext)
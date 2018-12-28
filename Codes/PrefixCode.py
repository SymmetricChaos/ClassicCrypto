# A prefix code is any code in which words can be of various lengths but which
# does not need commas to show the breaks between them. There are many ways to
# accomplish this. This example uses the Fibonnaci numbers. To keep the encoded
# text as short as possible short codes are given to common letters. However it
# is still not especially compact.

def fibonnaci(n):
    a = 1
    b = 1
    out = []
    for i in range(n):
        out.append(a)
        a,b = a+b,a
    return out

def makeCodebook(decode=False):
    F = fibonnaci(26)
    F.reverse()
    codes = []
    for x in range(27):
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
    D = makeCodebook(decode=decode)
    out = []
    for letter in text:
        out.append(D[letter])
    return "".join(out)

ptext = "THEQUICKBROWNFOXJUMPSPOVERTHELAZYDOG"
ctext = prefixCode(ptext)

print(ptext)
print(ctext)
print(len(ctext))
print(len(ptext)*5)

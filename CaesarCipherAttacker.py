def caesar(s,k,decode=False):
    s = s.upper()
    if decode == True:
        k = 26-k
    return "".join([chr((ord(i)-65+k)%26+65) for i in s])

ctext = caesar("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG",15)

for i in range(0,26):
    print(caesar(ctext,i,decode=True))
from Ciphers.UtilityFunctions import groups

# A route cipher works simply by writing down the message and then reading it
# off in some unusual order.  There are a tremendous number of possible route
# route ciphers this one is very simple. The text is written left to right into
# a certain number of columns then reading up and down the columns like a
# snake.
        
# THEQUIC
# KBROWNF
# OXJUMPS
# OVERTHE
# LAZYDOG

# TKOOL AVXBH ERJAZ YRUOQ UWMTD OHPNI CFSEG
        
def routeCipher(text,key,decode=False):
    while len(text) % key != 0:
        text += "X"
    
    if decode == False:
        G = groups(text,key)
        out = ""
        ctr = 0
        while ctr < key:
            gr = []
            for i in G:
                gr.append(i[ctr])
            if ctr % 2 == 1:
                gr.reverse()
            out += "".join(gr)
            ctr += 1
    
        return out
    
    if decode == True:
        
        key = len(text)//key
        
        G = groups(text,key)
        
        out = ""
        
        for passthru in range(key):
            for pos,lets in enumerate(G):

                if pos % 2 == 0:
                    a = lets[0]
                    G[pos] = lets[1:]

                if pos % 2 == 1:
                    a = lets[-1]
                    G[pos] = lets[:-1]

                out += a

        return out
    
def routeCipherExample():

    print("Route Cipher Example")
    key = 12
    print("The Key Is {}".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = routeCipher(ptext,key)
    dtext = routeCipher(ctext,key,decode=True)
    print("Plaintext is:  {}".format(ptext))
    print("Ciphertext is: {}".format(ctext))
    print("Decodes As:    {}".format(dtext))
import random

def step(R,n):
    x = R[:]
    for i in range(n):
        x = x[1:] + x[0]
    return x


def cipherdisk(text,key,decode=False):
    outer = "ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789"
    inner = "1yw7usq2om8kig3eca9bd4fhj0lnp5rtvx6z"

    inner = step(inner,key)
    
    if decode == False:
        out = ""
        for i in text:
            out += inner[outer.index(i)]
            if random.random() < .1:
                R = random.choice("123456789")
                out += R
                inner = step(inner,int(R))
        return out
    
    if decode == True:
        out = ""
        for i in text:
            dec = outer[inner.index(i)]
            if dec in "123456789":
                inner = step(inner,int(dec))
            else:
                out += dec
        return out

    
ptext = "THEQUICKBROWNFOX"
ctext = cipherdisk(ptext,10)
print(ctext)
print()
dtext = cipherdisk(ctext,10,decode=True)
print(dtext)
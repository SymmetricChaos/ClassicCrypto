import random

# The cipher disk method of encryption makes a lot of sense to treat as an
# object oriented program.

class cipherDisk:
    
    def __init__(self,inner,start,gaprange,turn):
        self.inner = inner
        self.outer = "ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789"
        self.gaprange = gaprange
        self.turn = turn
        self.start = start
        
    def rotate(self,n):
        for i in range(n):
            self.inner = self.inner[1:] + self.inner[0]
    
    def start_position(self,key):
        while self.inner[0] != key:
            self.rotate(1)
    
    def encrypt_letter(self,letter):
        return self.inner[self.outer.index(letter)]
        
    def encrypt_message(self,text):
        
        self.start_position(self.start)
        
        out = []
        
        gap = random.randint(self.gaprange[0],self.gaprange[1])
    
        for letter in text:
            
            out.append( self.encrypt_letter(letter) )
            
            gap -= 1
            if gap == 0:
                R = random.choice("0123456789")
                out.append( self.encrypt_letter(R) )
                self.rotate(int(R))
                gap = random.randint(self.gaprange[0],self.gaprange[1])
            self.rotate(self.turn)
            
        return "".join(out)
    
    def decrypt_letter(self,letter):
        return self.outer[self.inner.index(letter)]
    
    def decrypt_message(self,text):
        
        self.start_position(self.start)
        
        out = []
        for letter in text:
            pt = self.decrypt_letter(letter)
            if pt in "0123456789":
                self.rotate(int(pt))
            else:
                out.append(pt)
            self.rotate(self.turn)
            
        return "".join(out)
        
D = cipherDisk("1YW7USQ2OM8KIG3ECA9BD4FHJ0LNP5RTVX6Z","K",[5,7],1)


ptext = "THEQUICKBROWNFOX"
ctext = D.encrypt_message(ptext)
dtext = D.decrypt_message(ctext)

print(ptext)
print(ctext)
print(dtext)


# The M209 was, in sense, one of the simplest of the cipher machines as it was
# operated entirely mechanically. However the machine settings were extremely
# elaborate.

def M209(text,key,decode=False):
    
    pins = key[0]
    lugs = key[0]
    
    R1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    R2 = "ABCDEFGHIJKLMNOPQRSTUVXYZ" 
    R3 = "ABCDEFGHIJKLMNOPQRSTUVX"
    R4 = "ABCDEFGHIJKLMNOPQRSTU"
    R5 = "ABCDEFGHIJKLMNOPQRS"
    R6 = "ABCDEFGHIJKLMNOPQ"
    
    
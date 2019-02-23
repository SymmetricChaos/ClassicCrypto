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
    


def M209Example():
    
    import random
    
    # Pins can be in either effective + or ineffective - positions
    pins = []
    for p in [26,25,23,21,19,17]:
         pins.append(random.choices("-+",k=p))
    
    for i in pins:
        print("".join(i))
    
    # There are 27 pairs of lugs 
    # They can be in one of six effective positions or in one of two ineffective
    # positions. Both lugs can be ineffective but both cannot be assigned to the
    # save effective position.
    # REMEMBER PYTHON ARRAYS START AT ZERO BUT M209 SPECIFICATION STARTS AT 1
    lugs = []
    for l in range(27):
        
        lugs.append(random.sample([0,0,1,2,3,4,5,6],k=2))
    
    for i in lugs:
        print(i)
M209Example()
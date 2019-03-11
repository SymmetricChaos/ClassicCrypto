from Ciphers.RotorMachine import M209

def M209Example():
    
    #import random
    #random.seed(1)
    # Pins can be in either effective + or ineffective - positions
    #pins = []
    #for p in [26,25,23,21,19,17]:
    #     pins.append(random.choices("-+",k=p))
    
    # There are 27 pairs of lugs 
    # They can be in one of six effective positions or in one of two ineffective
    # positions. Both lugs can be ineffective but both cannot be assigned to the
    # save effective position.
    # REMEMBER PYTHON ARRAYS START AT ZERO BUT M209 SPECIFICATION STARTS AT 1
    
    #lugs = []
    #for l in range(27):  
    #    lugs.append(random.sample([0,0,1,2,3,4,5,6],k=2))

    #        ABCDEFGHIJKLMNOPQRSTUVWXYZ
    pins = ["++-+---++-+-++----++-++---",
            "+--++-+--+++--+--++-+-+--",
            "++----++-+-+++---++++-+",
            "--+-++-++---++-+--+++",
            "-+-+++-++---++-+--+",
            "++-+---+--+--++-+"]

    lugs = [[3,6], [0,6], [1,6], [1,5], [4,5], [0,4], [0,4],
            [0,4], [0,4], [2,0], [2,0], [2,0], [2,0], [2,0],
            [2,0], [2,0], [2,0], [2,0], [2,0], [2,5], [2,5],
            [0,5], [0,5], [0,5], [0,5], [0,5], [0,5]]

    ptext = "THEZQUICKZBROWNZDOGZJUMPSZOVERZTHEZLAZYZDOG"
    ctext = M209(ptext,["TABLEA",pins,lugs])
    dtext = M209(ctext,["TABLEA",pins,lugs])
    print(ptext)
    print(ctext)
    print(dtext)
    
M209Example()
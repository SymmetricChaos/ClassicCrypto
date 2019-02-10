from Ciphers.UtilityFunctions import groups, baseConvert

# Using the ASCII 1967 standard.
def ASCII(text, decode = False, mode = "BIN"):
    
    # We use Python's triple quotes so that its possible to include " and '
    chars = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    
    if decode == False:
        for let in text:
            if let not in chars:
                raise Exception("{} is not part of the ASCII67 standard")
    
    if decode == True:
        for let in text:
            if let not in "01":
                raise Exception("Must be a sequence of 0s and 1s")
                
                
print(baseConvert(74,10))
print(baseConvert(74,9))
print(baseConvert(174,2))
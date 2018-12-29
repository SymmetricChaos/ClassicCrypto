from PolybiusSquare import polybiusSquare

# The bifid cipher is a very simple composite cipher that uses the polybius
# square followed by a simple transposition followed by the polybius square
# in reverse.

def bifidCipher(text,key,decode=False):
    
    nums = polybiusSquare(text,key)

    if decode == False:
  
        A = ""
        B = ""
        for i in range(len(text)):
            A += nums[i*2]
            B += nums[i*2+1]
        return polybiusSquare(A+B,key,decode=True)

    if decode == True:
        A = nums[:len(nums)//2]
        B = nums[len(nums)//2:]
        out = "".join([i+j for i,j in zip(A,B)])
    
        return polybiusSquare(out,key,decode=True)


ptext = "THEQUICKBROWNFOX"
ctext = bifidCipher(ptext,"ZEBRAS")
dtext = bifidCipher(ctext,"ZEBRAS",decode=True)

print(ptext)
print(ctext)
print(dtext)
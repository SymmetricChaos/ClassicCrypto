from Ciphers import cipherDisk
from Ciphers.CipherDisk import stepN
    
def cipherDiskExample():

    print("Example of a Cipher Disk\n")
    
    inner = "1YW7USQ2OM8KIG3ECA9BD4FHJ0LNP5RTVX6Z"
    start = "K"
    inStart = inner[:]
    while inStart[0] != start:
        inStart = stepN(inStart,1)
    print("Inner Ring Is:\n{}".format(inner))
    print("Rotated To Start Position {}:\n{}\n".format(start,inStart))

    key = [inner,start]

    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = cipherDisk(ptext,key)
    dtext = cipherDisk(ctext,key,decode=True)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    print("Decodes As:\n{}".format(dtext))
    
cipherDiskExample()
from Ciphers.Transposition import columnarTransport, doubleColumnarTransport
from Ciphers.UtilityFunctions import addNulls, uniqueRank
from Tests.ExampleTemplate import example



def columnarTransportExample():
    
    print("Example of the columnar transport cipher.")

    print("Columnar Transport Example")
    key = "BIRTHDAYS"
    print("The Key Is {}".format(key))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    example(columnarTransport,ptext,key,complete=False)
    
    example(columnarTransport,ptext,key,complete=True)
    
    
def doubleColumnarTransportExample():

    print("Double Columnar Transport Example")
    keys = ["ILIKEEGGS","BLAHDIBLAHBLAH"]
    print("The Key Is {}".format(keys))
    
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    ctext = doubleColumnarTransport(ptext,keys)
    dtext = doubleColumnarTransport(ctext,keys,decode=True)
    print("Plaintext is:\n{}".format(ptext))
    print("Ciphertext is:\n{}".format(ctext))
    print("Decodes As:\n{}".format(dtext))

columnarTransportExample()
#doubleColumnarTransportExample()

from Ciphers.Transposition import columnarTransport, doubleColumnarTransport
from Ciphers.UtilityFunctions import addNulls, uniqueRank, groups
from Tests.ExampleTemplate import example



def columnarTransportExample():
    
    print("Example of the columnar transport cipher")

    key = "BIRTHDAY"
    ptext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    rank = uniqueRank(key)
    
    
    print("\nThe Key Is {}".format(key))
    
    print("Each letter of the key is ranked to get")
    print(*rank)

    print("\nThe plaintext is\n{}".format(ptext))
    ptext = addNulls(ptext,40)
    
    print("\nNow the text is read into columns with some nulls added with they key above it.")

    print("".join([str(i) for i in rank]))
    for i in groups(ptext,8):
        print(i)


    
    #example(columnarTransport,ptext,key,complete=False)
    
    #example(columnarTransport,ptext,key,complete=True)
    
    
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

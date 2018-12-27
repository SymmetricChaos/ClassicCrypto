# A composite cipher is simply the application of multiple ciphers in sequence
# in order to make decoding more difficult. This is usually beneficial as
# ciphers of different kinds can interfere with methods used for attacking
# others.

# A few available ciphers are already composite. The multiVigenere cipher and
# doubleColumnarTransport both apply the same form of encryption repeatedly in
# order to gain a somewhat lesser benefit.

def compositeCipher(text,ciphers,keys,decode=False):
    if len(ciphers) > len(keys):
        raise Exception('every cipher needs a key')
    if len(keys) > len(ciphers):
        raise Exception('too many keys provided')
    
    ctext = text
    if decode == False:
        for cipher,key in zip(ciphers,keys):
            ctext = cipher(ctext,key)
        return ctext

    dtext = text
    if decode == True:
        ciphers.reverse()
        keys.reverse()
        for cipher,key in zip(ciphers,keys):
            dtext = cipher(dtext,key,decode=True)
        return dtext    

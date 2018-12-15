# ClassicCrypto
Python repo for implementing classic methods of encryption and techniques for breaking them.

All implemented ciphers are functions of the form cipherName(text,key,decode=False)
  text must be a string
  key is whatever kind of key the cipher uses, if it requires multiple keys they must be in a list
  decode is boolean and sets the function to either encode or decode
There are currently no guarantees on what the cipher functions return. Most give a string but a few return a list. For example the nomenclator cipher returns a list that contains the encoded or decoded text along with a dictionary that serves as the key.

This is a hobby project. Suggestions for improvements are welcome but I'm prioritizing clarity and explicitness over things like checking for valid inputs.

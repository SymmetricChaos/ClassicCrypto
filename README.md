# ClassicCrypto
Python repo for implementing classic methods of encryption and techniques for breaking them.

All implemented ciphers are functions of the form cipherName(text,key,decode=False)
  text must be a string
  key is whatever kind of key the cipher uses, if it requires multiple keys they must be in a list
  decode is boolean and sets the function to either encode or decode
All ciphers will return a string containing either the ciphertext or the decoded text.
The nomenclator cipher has an alternate mode that returns the dictionary that serves as the internal key.

Available Ciphers:
  Caesar and Affine ciphers
Simple Substitution cipher
Columnar Transport and Double Columnar Transport
Rail Fence Cipher
Hill's Matrix Cipher
Vigenre Cipher
Affine Vigenere Cipher using an extended 37 letter alphabet
Vigenre Autokey Cipher
Multiple Vigenre Cipher
Nomenclator cipher

Available Attacks:
Kasiski Examination attack on the Vigenere cipher
Brute force attack on Columnar Transport
Brute force attack on Caesar cipher


This is a hobby project. Suggestions for improvements are welcome but I'm prioritizing clarity and explicitness over things like speed or checking for valid inputs.

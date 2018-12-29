# ClassicCrypto
Python repo for implementing classic methods of encryption and techniques for breaking them.
Requires Numpy.

## Classical Cryptography
The term "classical cryptography" refers broadly to two different concepts.
* Firstly it is used for ciphers that allow an ordinary person to encrypt and decrypt a useful amount of information in a reasonable amount of time without anything but simple tools. Most of the ciphers presented here are of that form. Using a computer many of these techniques can be performed much faster and more accurately.
* Secondly classical cryptography includes any method of cryptography that is no longer considered to be secure in practice. This includes devices like the Enigma machine from World War II but also much more recent ciphers such as RC4 and DES. For the purpose of this project the era of classical cryptography is ended, somewhat arbitrarily, in 1950 following the publication of "A Mathematical Theory of Cryptography" by Claude Shannon.


## Details
All implemented ciphers are functions of the form `cipherName(text,key,decode=False)`
*  `text` must be a string
*  `key` is whatever kind of key the cipher uses, if it requires multiple keys they must be in a list
*  `decode` is boolean and sets the function to either encode or decode

All ciphers will return a string containing either the ciphertext or the decoded text.
The nomenclator cipher has an alternate mode that returns the dictionary that serves as the internal key.

###  Ciphers:
* Caesar cipher
* Affine cipher
* Simple Substitution cipher
* Hill's Matrix Cipher
* Vigenere Cipher
* Affine Vigenere Cipher (extended 37 letter alphabet)
* Vigenere Autokey Cipher
* Multiple Vigenere Cipher
* Nomenclator cipher (variation on Le Grand Chiffre)
* Polybius Square (IJ, CK, and extended alphabet versions)
* Straddling Checkerboard
* Nihilist Cipher
* ADFGX and ADFGVX
* Simple Rotor Machine (styled after Engima but not a simulator)
* Columnar Transport (Single and Double)
* Rail Fence Cipher
* DRYAD
* Bifid

### Codes:
* Morse Code
* Godel Numbering
* Bacon Cipher
* Prefix Code

### Available Attacks:
* Kasiski Examination attack on the Vigenere cipher
* Brute force attack on Columnar Transport
* Brute force attack on Caesar cipher


This is a hobby project. Suggestions for improvements are welcome but I'm prioritizing clarity and explicitness over things like speed or checking for valid inputs.

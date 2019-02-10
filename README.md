# ClassicCrypto
Python repo for implementing classic methods of encryption and techniques for breaking them. This is a hobby project. Suggestions for improvements are welcome but I'm prioritizing clarity and explicitness over things like speed or checking for valid inputs.

## Classical Cryptography
The term "classical cryptography" refers broadly to two different concepts.
* Firstly it is used for ciphers that allow an ordinary person to encrypt and decrypt a useful amount of information in a reasonable amount of time without anything but simple tools. Most of the ciphers presented here are of that form. Using a computer many of these techniques can be performed much faster and more accurately.
* Secondly classical cryptography includes any method of cryptography that is no longer considered to be secure in practice. This includes devices like the Enigma machine from World War II but also much more recent ciphers such as RC4 and DES. For the purpose of this project the era of classical cryptography is ended, somewhat arbitrarily, in 1950 following the publication of "A Mathematical Theory of Cryptography" by Claude Shannon.

## Codes vs Ciphers
The difference between codes and ciphers in classical cryptography is fairly vague, indeed the terms are sometimes used interchangeably. Within this project a cipher must have a changeable key that is needed in order to determine the plaintext. A code on the otherhand is fixed and can be read by anyone who knows the method.

## Details
All ciphers are functions of the form `cipherName(text,key,decode=False)`
*  `text` must be a string with either plaintext or ciphertext
*  `key` is whatever kind of key the cipher uses, if it requires multiple keys they must be in a list
*  `decode` is boolean and sets the function to either encode or decode

All ciphers will return a string containing either the ciphertext or the decoded text.

Ciphers based on the Polybius Square or on the Playfair Cipher have the argument `mode` which can be:
*  `IJ` replaces J with I to get a 25 letter square
*  `CK` replaces C with K to get a 25 letter square
*  `QK` replaces Q with K to get a 25 letter square
*  `EX` appends the digits 0 to 9 to the alphabet to get a 36 letter alphabet

The nomenclator cipher has an alternate mode that returns the dictionary that serves as the internal key.

Each cipher has an example of the form `cipherNameExample()` which gives a quick example of the cipher and the kind of key it uses. A few ciphers provide additional information about how the cipher is used.

##  Ciphers:

#### Monoalphabetic Substitution:
* Substitution cipher
* Atbash
* Caesar cipher
* ROT13
* Affine cipher

#### Vigenere Variants:
* Vigenere Cipher
* Affine Vigenere Cipher
* Autokey Cipher
* Beaufort Cipher

#### Polybius Square Variants:
* Polybius Square
* ADFGX and ADFGVX
* Bifid and Trifid
* Nihilist Cipher

#### Playfair Type Cipher
* Playfair Cipher
* Two Square Cipher
* Four Square Cipher

#### Rotor Machines
* Enigma

#### Other Substitution Ciphers
* Hill's Matrix Cipher
* DRYAD
* Straddling Checkerboard
* Cipher Disk
* Disrupted Tableau

#### Transposition Ciphers
* Columnar Transport
* Rail Fence Cipher
* Route Cipher
* Turning Grille

#### Variable Codebooks
* Nomenclator (variation on Le Grand Chiffre)

#### Composite Ciphers:
* Checkboard/DRYAD
* Vigenere/Columnar

## Codes:

#### Binary Codes:
* Bacon Code
* Prefix Code
* Binary Braille
* Binary Morse

#### Other Codes:
* Godel Numbering
* Brevity Code
* Braille
* Morse Code
* Bacon Cipher (using any binary code)

## Random Number Generators:
* Reihenschieber
* Weyel Sequence
* Linear Congruential Generator

## Available Attacks:

#### Brute Force
* Columnar Transport
* Caesar Cipher
* Affine Cipher

#### Other Techniques
* Vigenere
* Simple Substitution
* Autokey
* Hill Cipher

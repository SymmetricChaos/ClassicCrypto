import tkinter as tk
from Ciphers.Vigenere import vigenere

root = tk.Tk()
root.maxsize(800,800)
root.minsize(800,800)
root.title("Vigenere Cipher")
ptext = tk.Text(root,height=4,width=40)
ctext = tk.Text(root,height=4,width=40)
key = tk.Text(root,height=1,width=20)

# Encrypt
def enc(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    k = key.get("1.0","end")[:-1]
  
    ctext.insert("insert",vigenere(T,k,decode=True)) 

# Decrypt       
def dec(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    k = key.get("1.0","end")[:-1]
    
    ctext.insert("insert",vigenere(T,k,decode=False)) 
  
# Button to run cipher in encrypt mode
encryptbutton = tk.Button(root, text="Encrypt", command = enc)

# Button to run cipher in decrypt mode
decryptbutton = tk.Button(root, text="Decrypt", command = dec)


ptextLab = tk.Label(root,text="Plaintext")
ctextLab = tk.Label(root,text="Ciphertext")
keyLab = tk.Label(root,text="Key")


ptext.place(x=150,y=30)
ptextLab.place(x=90,y=30)

key.place(x=150,y=120)
keyLab.place(x=120,y=120)

encryptbutton.place(x=150,y=160)
decryptbutton.place(x=220,y=160)

ctextLab.place(x=85,y=200)
ctext.place(x=150,y=200)
root.mainloop()
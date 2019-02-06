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
  
# Show message button 
encryptbutton = tk.Button(root, text="Encrypt", command = enc)

# Show message button 
decryptbutton = tk.Button(root, text="Decrypt", command = dec)

ptext.pack()
key.pack()
encryptbutton.pack()
decryptbutton.pack()
ctext.pack()
root.mainloop()
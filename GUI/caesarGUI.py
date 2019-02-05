import tkinter as tk
from Ciphers.Caesar import caesar

root = tk.Tk()
root.maxsize(800,800)
root.minsize(800,800)
root.title("Caesar Cipher")
ptext = tk.Text(root)
ctext = tk.Text(root)
key = tk.Text(root)
encryptbutton = tk.Button(root, text="Encrypt", command = lambda: caesarText(ptext,ctext,key))

def caesarText(textIn,textOut,key):
    k = key.get("1.0","end")[:-1]
    theInput = textIn.get("1.0","end")[:-1]
    textOut.delete("1.0","end")
    textOut.insert("insert",caesar(theInput,k,decode=False))

ptext.pack()
encryptbutton.pack()
key.pack()
ctext.pack()
root.mainloop()
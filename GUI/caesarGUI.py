import tkinter as tk
from Ciphers.Caesar import caesar

root = tk.Tk()
root.maxsize(18001,800)
root.minsize(1800,1800)
root.title("Caesar Cipher")
ptext = tk.Text(root,height=2,width=20)
ctext = tk.Text(root,height=2,width=20)
key = tk.Text(root,height=1,width=20)
encryptbutton = tk.Button(root, text="Encrypt", command = lambda: caesarText(ptext,ctext,key))

def caesarText(textIn,textOut,key):
    k = key.get("1.0","end")[:-1]
    theInput = textIn.get("1.0","end")[:-1]
    textOut.delete("1.0","end")
    textOut.insert("insert",caesar(theInput,k,decode=False))

ptext.pack()
key.pack()
encryptbutton.pack()
ctext.pack()
root.mainloop()
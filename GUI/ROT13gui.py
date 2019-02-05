import tkinter as tk
from Ciphers.Caesar import ROT13
root = tk.Tk()
root.maxsize(800,800)
root.minsize(800,800)
root.title("ROT13")
ptext = tk.Text(root)
ctext = tk.Text(root)
reversebutton = tk.Button(root, text="Encrypt", command = lambda: ROT13IT(ptext,ctext))

def ROT13IT(textIn,textOut):
    theInput = textIn.get("1.0","end")[:-1]
    textOut.delete("1.0","end")
    textOut.insert("insert",ROT13(theInput))
    
ptext.pack()
reversebutton.pack()
ctext.pack()
root.mainloop()
import tkinter as tk
from Ciphers.Caesar import caesar

root = tk.Tk()
root.maxsize(800,800)
root.minsize(800,800)
root.title("Caesar Cipher")
ptext = tk.Text(root,height=4,width=40)
ctext = tk.Text(root,height=4,width=40)
key = tk.Text(root,height=1,width=20)

# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.set("")
    ptext.set("") 
    key.set("") 
  

# Encrypt function
def enc(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    k = key.get("1.0","end")[:-1]
  
    ctext.insert("insert",caesar(T,k,decode=True)) 

# Decrypt function 
def dec(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    k = key.get("1.0","end")[:-1]
    
    ctext.insert("insert",caesar(T,k,decode=False)) 
  
# Button to run cipher in encrypt mode
encryptbutton = tk.Button(root, text="Encrypt", command = enc,
                          bg = 'lightblue', font = ('arial',14,'bold'))

# Button to run cipher in decrypt mode
decryptbutton = tk.Button(root, text="Decrypt", command = dec,
                          bg = 'lightgreen', font = ('arial',14,'bold'))


# Button to run cipher in decrypt mode
exitbutton = tk.Button(root, text="Exit", command = qExit, 
                       bg = 'salmon', font = ('arial',14,'bold'))


# Labels
# MAKE THESE LOOK BETTER
ptextLab = tk.Label(root,text="Plaintext:",font = ('arial',14))
ctextLab = tk.Label(root,text="Ciphertext:",font = ('arial',14))
keyLab = tk.Label(root,text="Key:",font = ('arial',14))


ptext.place(x=150,y=30)
ptextLab.place(x=50,y=30)

key.place(x=150,y=120)
keyLab.place(x=80,y=115)

encryptbutton.place(x=150,y=160)
decryptbutton.place(x=250,y=160)

ctext.place(x=150,y=220)
ctextLab.place(x=40,y=220)

exitbutton.place(x=150,y=320)

root.mainloop()
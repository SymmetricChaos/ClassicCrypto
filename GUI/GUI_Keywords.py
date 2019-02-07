import tkinter as tk
from Ciphers.Vigenere import vigenere
from Ciphers.Playfair import playfair
from Ciphers.Autokey import autokey
from Ciphers.Beaufort import beaufort
from Ciphers.Substitution import substitution

root = tk.Tk()

root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("Keyword Ciphers")

# Three textboxes
ptext = tk.Text(root,height=4,width=40)
ctext = tk.Text(root,height=4,width=40)
key = tk.Text(root,height=1,width=20)

# Dropdown Menu
cipher = tk.StringVar(root)
cipher.set("choose a cipher")
selecter = tk.OptionMenu(root,cipher,"vigenere","beaufort","autokey","playfair","substitution")

# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.delete("1.0","end")
    ptext.delete("1.0","end") 
    key.delete("1.0","end") 
  

# Encrypt function
def enc(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    k = key.get("1.0","end")[:-1]
    
    # Get the selected cipher
    C = cipher.get()
    
    # We use a dictionary as basically a as a switch statement
    # They keys are the names of the cipher while the values are the cipher
    # functions that we imported
    cipherDict = {"vigenere": vigenere,
                  "beaufort": beaufort,
                  "autokey": autokey,
                  "playfair": playfair,
                  "substitution": substitution}
  
    # Blank the ctext box then put the text in it
    ctext.delete("1.0","end")
    ctext.insert("insert",cipherDict[C](T,k,decode=True)) 

# Decrypt function 
def dec(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    k = key.get("1.0","end")[:-1]
    
    # Blank the ctext box then put the text in it
    ctext.delete("1.0","end")
    ctext.insert("insert",vigenere(T,k,decode=False)) 
  
# Button to run cipher in encrypt mode
encryptbutton = tk.Button(root, text="Encrypt", command = enc,
                          bg = 'lightblue', font = ('arial',14,'bold'))

# Button to run cipher in decrypt mode
decryptbutton = tk.Button(root, text="Decrypt", command = dec,
                          bg = 'lightgreen', font = ('arial',14,'bold'))


resetbutton = tk.Button(root, text="Reset", command = Reset, 
                       bg = 'lightslateblue', font = ('arial',14,'bold'))


# Button to run cipher in decrypt mode
exitbutton = tk.Button(root, text="Exit", command = qExit, 
                       bg = 'salmon', font = ('arial',14,'bold'))


# Labels
# MAKE THESE LOOK BETTER
ptextLab = tk.Label(root,text="Plaintext:",font = ('arial',14))
ctextLab = tk.Label(root,text="Ciphertext:",font = ('arial',14))
keywordLab = tk.Label(root,text="Keyword:",font = ('arial',14))

selecter.place(x=550,y=30)

ptext.place(x=150,y=30)
ptextLab.place(x=60,y=30)

key.place(x=150,y=120)
keywordLab.place(x=60,y=115)

encryptbutton.place(x=150,y=160)
decryptbutton.place(x=250,y=160)
resetbutton.place(x=400,y=160)

ctext.place(x=150,y=220)
ctextLab.place(x=50,y=220)

exitbutton.place(x=150,y=320)

root.mainloop()
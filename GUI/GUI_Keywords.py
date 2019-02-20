import tkinter as tk

from Ciphers.Vigenere import vigenere
from Ciphers.Playfair import playfair
from Ciphers.Autokey import autokey
from Ciphers.Beaufort import beaufort
from Ciphers.Substitution import substitution
from Ciphers.UtilityFunctions import saveFormat, restoreFormat

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("Keyword Ciphers")

# Three textboxes
ptext = tk.Text(root,height=8,width=40)
key = tk.Text(root,height=1,width=20)
ctext = tk.Text(root,height=8,width=40)

# Dropdown menu with ciphers
cipher = tk.StringVar(root)
cipher.set("substitution")
cipherMenu = tk.OptionMenu(root,cipher,"substitution","vigenere","beaufort","autokey","playfair")

# Tickbox to decide on formatting
form = tk.IntVar(root)
form.set(1)
formMenu = tk.Checkbutton(root, text="Keep Formatting", variable=form)


# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.delete("1.0","end")
    ptext.delete("1.0","end") 
    key.delete("1.0","end") 
  

# 
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

# Encrypt function
def enc(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    K = key.get("1.0","end")[:-1]
    K = K.upper()
    # Get the selected cipher
    C = cipher.get()
    # Get the formatting rule
    F = form.get()
    

    T, pos, char,case = saveFormat(T)
    
    # We use a dictionary as basically a as a switch statement
    # They keys are the names of the cipher while the values are the cipher
    # functions that we imported
    cipherDict = {"vigenere": vigenere,
                  "beaufort": beaufort,
                  "autokey": autokey,
                  "playfair": playfair,
                  "substitution": substitution}
  
    # Blank the ctext box
    ctext.delete("1.0","end")
    
    # Try encrypting
    try:
        tx = cipherDict[C](T,K,decode=False)
    except Exception as e:
        ctext.insert("insert",str(e)) 
    
    if F == 1:
        ctext.insert("insert",restoreFormat(tx, pos, char,case))
    else:
        ctext.insert("insert",tx)
         


# Decrypt function 
def dec(): 


    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    K = key.get("1.0","end")[:-1]
    K = K.upper()
    # Get the selected cipher
    C = cipher.get()
    # Get the formatting rule
    F = form.get()
    

    T, pos, char,case = saveFormat(T)
    
    # We use a dictionary as basically a as a switch statement
    # They keys are the names of the cipher while the values are the cipher
    # functions that we imported
    cipherDict = {"vigenere": vigenere,
                  "beaufort": beaufort,
                  "autokey": autokey,
                  "playfair": playfair,
                  "substitution": substitution}
  
    # Blank the ctext box
    ctext.delete("1.0","end")
    
    # Try encrypting
    try:
        tx = cipherDict[C](T,K,decode=True)
    except Exception as e:
        ctext.insert("insert",str(e)) 
    
    if F == 1:
        ctext.insert("insert",restoreFormat(tx, pos, char,case))
    else:
        ctext.insert("insert",tx)
        

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
ptextLab = tk.Label(root,text="Input:",font = ('arial',14))
ctextLab = tk.Label(root,text="Output:",font = ('arial',14))
keywordLab = tk.Label(root,text="Keyword:",font = ('arial',14))
explainLab = tk.Label(root,
                      text="The key must consist of english letters.",
                      font = ('arial',12),
                      wraplength=200,
                      relief=tk.GROOVE,
                      padx = 10, pady = 10)
cipherLab = tk.Label(root,text="Cipher:",font = ('arial',12))

# Tab control
ptext.bind("<Tab>", focus_next_widget)
key.bind("<Tab>", focus_next_widget)
ctext.bind("<Tab>", focus_next_widget)

# Put everything in position
cipherMenu.place(x=590,y=65)
cipherLab.place(x=530,y=70)
formMenu.place(x=530,y=40)

explainLab.place(x=550,y=200)

ptext.place(x=150,y=30)
ptextLab.place(x=60,y=30)

key.place(x=150,y=200)
keywordLab.place(x=60,y=200)

encryptbutton.place(x=150,y=240)
decryptbutton.place(x=250,y=240)
resetbutton.place(x=400,y=240)

ctext.place(x=150,y=300)
ctextLab.place(x=50,y=300)

exitbutton.place(x=150,y=450)

root.mainloop()
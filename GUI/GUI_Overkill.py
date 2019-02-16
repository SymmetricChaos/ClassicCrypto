import tkinter as tk

from Ciphers.Nomenclator import nomenclator
from Ciphers.UtilityFunctions import preptext

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(1200,800)
root.minsize(1200,800)

# Title of the window
root.title("The Overkill Cipher")

# Three textboxes
ptext = tk.Text(root,height=8,width=40)
key = tk.Text(root,height=1,width=16)
ctext = tk.Text(root,height=12,width=40)


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
    T = preptext(T)
    # Get the key from the key box
    K = key.get("1.0","end")[:-1]

    
    # Blank the ctext box
    ctext.delete("1.0","end")
    
    # Try encrypting
    try:
        tx = nomenclator(T,K,decode=False)
    except Exception as e:
        ctext.insert("insert",str(e)) 
    
    ctext.insert("insert",tx)
         


# Decrypt function 
def dec(): 


    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    K = key.get("1.0","end")[:-1]
    
  
    # Blank the ctext box
    ctext.delete("1.0","end")
    
    # Try encrypting
    try:
        tx = nomenclator(T,K,decode=True)
    except Exception as e:
        ctext.insert("insert",str(e)) 
    
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
keywordLab = tk.Label(root,text="Shuffle:",font = ('arial',14))
explainLab = tk.Label(root,
                      text="All symbols except letters from the standard English alphabet will be removed.",
                      font = ('arial',12),
                      wraplength=200,
                      relief=tk.GROOVE,
                      padx = 10, pady = 10)
cipherLab = tk.Label(root,text="Cipher",font = ('arial',11))
formLab = tk.Label(root,text="Formatting",font = ('arial',11))

# Tab control
ptext.bind("<Tab>", focus_next_widget)
key.bind("<Tab>", focus_next_widget)
ctext.bind("<Tab>", focus_next_widget)

# Put everything in position
cipherLab.place(x=530,y=50)
formLab.place(x=530,y=100)

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
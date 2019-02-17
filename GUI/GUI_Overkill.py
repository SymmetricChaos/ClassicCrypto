import tkinter as tk

from Ciphers.Nomenclator import nomenclator
from Ciphers.UtilityFunctions import preptext
import webbrowser

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,800)
root.minsize(800,800)

# Title of the window
root.title("The Overkill Cipher")

# Three textboxes
ptext = tk.Text(root,height=16,width=44)
key = tk.Text(root,height=1,width=16)
ctext = tk.Text(root,height=16,width=44)


# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.delete("1.0","end")
    ptext.delete("1.0","end") 
    key.delete("1.0","end") 

def link(event):
    webbrowser.open_new(r"https://github.com/SymmetricChaos/ClassicCrypto")

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
        tx = nomenclator(T,int(K),decode=False)
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
        tx = nomenclator(T,int(K),decode=True)
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
keywordLab = tk.Label(root,text="Key:",font = ('arial',14))
explainLab = tk.Label(root,
                      text="All symbols except letters from the standard English alphabet will be removed.",
                      font = ('arial',12),
                      wraplength=200,
                      relief=tk.GROOVE,
                      padx = 10, pady = 10)
linkLab = tk.Label(root, text="See The Code", 
                   font = ('courier',12),
                   relief=tk.GROOVE,
                   padx = 5, pady = 5,
                   fg="blue", cursor="hand2")

# Tab control
ptext.bind("<Tab>", focus_next_widget)
key.bind("<Tab>", focus_next_widget)
ctext.bind("<Tab>", focus_next_widget)

# Put everything in position
linkLab.place(x=620,y=730)
linkLab.bind("<Button-1>", link)

explainLab.place(x=550,y=100)

ptext.place(x=150,y=30)
ptextLab.place(x=60,y=30)

key.place(x=150,y=300)
keywordLab.place(x=60,y=300)

encryptbutton.place(x=150,y=330)
decryptbutton.place(x=250,y=330)
resetbutton.place(x=430,y=330)

ctext.place(x=150,y=380)
ctextLab.place(x=50,y=380)

exitbutton.place(x=150,y=700)

root.mainloop()
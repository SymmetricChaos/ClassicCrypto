import tkinter as tk

from Ciphers.Autokey import autokey

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("Autokey Example")

# Three textboxes
ptext = tk.Text(root,height=4,width=40)
key = tk.Text(root,height=1,width=20)
ctext = tk.Text(root,height=4,width=40)

# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.delete("1.0","end")
    ptext.delete("1.0","end") 
    key.delete("1.0","end") 
  

# Tab between things
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

# Encrypt function
def enc(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    k = key.get("1.0","end")[:-1]
  
    # Create the keystream
    kstream = k+T
    
    keystreamLab.config(text=" ".join(kstream[:20]))
    txtstreamLab.config(text=" ".join(T))
    
    out = autokey(T,k,decode=False)
    
    ctxstreamLab.config(text=" ".join(out)) 

# Decrypt function 
def dec(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box
    k = key.get("1.0","end")[:-1]
  
    # Create the keystream
    kstream = k+T
    
    keystreamLab.config(text=" ".join(kstream[:20]))
    txtstreamLab.config(text=" ".join(T))
    
    out = autokey(T,k,decode=True)
    
    ctxstreamLab.config(text=" ".join(out)) 
        

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
                      text="Both the input text and the key must consist of only uppercase letters taken from the standard English alphabet.",
                      font = ('arial',12),
                      wraplength=200,
                      relief=tk.GROOVE,
                      padx = 10, pady = 10)

keystreamLab = tk.Label(root,text="_ "*20,font = ('Courier',10))
addstreamLab = tk.Label(root,text="+ "*20,font = ('Courier',10))
txtstreamLab = tk.Label(root,text="_ "*20,font = ('Courier',10))
arrstreamLab = tk.Label(root,text="↓ "*20,font = ('Courier',10))
ctxstreamLab = tk.Label(root,text="_ "*20,font = ('Courier',10))



# Tabe control
ptext.bind("<Tab>", focus_next_widget)
key.bind("<Tab>", focus_next_widget)
ctext.bind("<Tab>", focus_next_widget)

# Put everything in position
explainLab.place(x=550,y=200)

ptext.place(x=150,y=30)
ptextLab.place(x=60,y=30)

key.place(x=150,y=110)
keywordLab.place(x=60,y=110)


txtstreamLab.place(x=150,y=200)
addstreamLab.place(x=150,y=220)
keystreamLab.place(x=150,y=240)
arrstreamLab.place(x=150,y=260)
ctxstreamLab.place(x=150,y=280)

encryptbutton.place(x=150,y=140)
decryptbutton.place(x=250,y=140)
resetbutton.place(x=400,y=140)

exitbutton.place(x=150,y=450)

root.mainloop()
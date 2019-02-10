import tkinter as tk

from Codes.ASCIICode import ASCII

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("ASCII Encodings")

# Three textboxes
ptext = tk.Text(root,height=7,width=40)
ctext = tk.Text(root,height=10,width=40)

# Dropdown Menu
mode = tk.StringVar(root)
mode.set("choose a code")
modeMenu = tk.OptionMenu(root,mode,"BIN","OCT","DEC","HEX","UTF")

# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.delete("1.0","end")
    ptext.delete("1.0","end") 
  

# Control movement between widgets
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

# Encrypt function
def enc(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]

    # Get the mode
    M = mode.get()
  
    # Blank the ctext box then put the text in it
    ctext.delete("1.0","end")
    ctext.insert("insert",ASCII(T,decode=False,mode=M)) 

# Decrypt function 
def dec(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    # Get the key from the key box

    # Get the mode
    M = mode.get()
  
    # Blank the ctext box then put the text in it
    ctext.delete("1.0","end")
    ctext.insert("insert",ASCII(T,decode=True,mode=M)) 
  
# Button to run cipher in encrypt mode
encryptbutton = tk.Button(root, text="Encode", command = enc,
                          bg = 'lightblue', font = ('arial',14,'bold'))

# Button to run cipher in decrypt mode
decryptbutton = tk.Button(root, text="Decode", command = dec,
                          bg = 'lightgreen', font = ('arial',14,'bold'))


resetbutton = tk.Button(root, text="Reset", command = Reset, 
                       bg = 'lightslateblue', font = ('arial',14,'bold'))


# Button to run cipher in decrypt mode
exitbutton = tk.Button(root, text="Exit", command = qExit, 
                       bg = 'salmon', font = ('arial',14,'bold'))


# Labels
ptextLab = tk.Label(root,text="Input:",font = ('arial',14))
ctextLab = tk.Label(root,text="Output:",font = ('arial',14))

# Tabe control
ptext.bind("<Tab>", focus_next_widget)
ctext.bind("<Tab>", focus_next_widget)

# Put everything in position
modeMenu.place(x=550,y=30)

ptext.place(x=150,y=30)
ptextLab.place(x=60,y=30)

encryptbutton.place(x=150,y=160)
decryptbutton.place(x=250,y=160)
resetbutton.place(x=400,y=160)

ctext.place(x=150,y=220)
ctextLab.place(x=50,y=220)

exitbutton.place(x=150,y=400)

root.mainloop()
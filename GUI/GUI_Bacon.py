import tkinter as tk

from Codes.MorseCode import binaryMorseCode
from Codes.BaconCode import baconCode
from Codes.PrefixCode import prefixCode
from Codes.ASCIICode import ASCII
from Codes.BaconCipher import baconCipher

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("Binary Codes")

# Three textboxes
ptext = tk.Text(root,height=5,width=40)
stego = tk.Text(root,height=5,width=40)
ctext = tk.Text(root,height=5,width=40)

# Dropdown Menu
code = tk.StringVar(root)
code.set("choose a code")
codeMenu = tk.OptionMenu(root,code,"morse","bacon","prefix","ASCII")

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
    S = stego.get("1.0","end")[:-1]

    # Get the selected cipher
    C = code.get()
    
    # We use a dictionary as basically a as a switch statement
    # They keys are the names of the cipher while the values are the cipher
    # functions that we imported
    codeDict = {"morse": binaryMorseCode,
                "bacon": baconCode,
                "prefix": prefixCode,
                "ASCII": ASCII}
  
    # Blank the ctext box then put the text in it
    ctext.delete("1.0","end")
    try:
        ctext.insert("insert",baconCipher(T,codeDict[C],S,decode=False)) 
    except Exception as e:
        ctext.insert("insert",str(e)) 

# Decrypt function 
def dec(): 

    # Get the text from the ptext box
    T = ptext.get("1.0","end")[:-1]
    S = stego.get("1.0","end")[:-1]

    # Get the selected cipher
    C = code.get()
    
    # We use a dictionary as basically a as a switch statement
    # They keys are the names of the cipher while the values are the cipher
    # functions that we imported
    codeDict = {"morse": binaryMorseCode,
                "bacon": baconCode,
                "prefix": prefixCode,
                "ASCII": ASCII}
  
    # Blank the ctext box then put the text in it
    ctext.delete("1.0","end")
    try:
        ctext.insert("insert",baconCipher(T,codeDict[C],S,decode=True)) 
    except Exception as e:
        ctext.insert("insert",str(e)) 
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
ptextLab = tk.Label(root,text="Your Text:",font = ('arial',14))
ctextLab = tk.Label(root,text="Output:",font = ('arial',14))
stegoLab = tk.Label(root,text="False Text:",font = ('arial',14))
explain = "Provide your text and a false text to hide it in. If you provide no false text then random letters will be used."
explainLab = tk.Label(root, text = explain,
                      font = ('arial',12),
                      wraplength=200,
                      relief=tk.GROOVE,
                      padx = 10, pady = 10)

# Tabe control
ptext.bind("<Tab>", focus_next_widget)
ctext.bind("<Tab>", focus_next_widget)

# Put everything in position
codeMenu.place(x=500,y=20)

ptext.place(x=150,y=30)
ptextLab.place(x=50,y=30)

stego.place(x=150,y=140)
stegoLab.place(x=40,y=140)


explainLab.place(x=550,y=200)

encryptbutton.place(x=150,y=250)
decryptbutton.place(x=250,y=250)
resetbutton.place(x=400,y=250)

ctext.place(x=150,y=300)
ctextLab.place(x=50,y=300)

exitbutton.place(x=150,y=400)

root.mainloop()
import tkinter as tk
import random
from Ciphers.Enigma import enigma
from Ciphers.UtilityFunctions import preptext

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("SIGABA Simulation")

# Textboxes
ptext = tk.Text(root,height=8,width=40)

reflector = tk.Text(root,height=1,width=20)
rotors = tk.Text(root,height=1,width=20)
positions = tk.Text(root,height=1,width=20)
plugboard = tk.Text(root,height=1,width=20)
ringsets = tk.Text(root,height=1,width=20)

ctext = tk.Text(root,height=8,width=40)

# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.delete("1.0","end")
    ptext.delete("1.0","end") 
    #cipherRotors.delete("1.0","end")
    #controlRotors.delete("1.0","end")
    #indexRotors.delete("1.0","end")
    #indicator.delete("1.0","end")
    #controlPos.delete("1.0","end")
    #indexPos.delete("1.0","end")

# Move between widgets
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")


# Get the key settings
def keysets():

    k1 = reflector.get("1.0","end")[:-1]
    k2 = rotors.get("1.0","end")[:-1]
    k3 = positions.get("1.0","end")[:-1]
    k4 = plugboard.get("1.0","end")[:-1]
    k5 = ringsets.get("1.0","end")[:-1]
    
    return [k1,k2,k3,k4,k5]


# Get the text from the ptext box and prepare it
def gettext():
    T = ptext.get("1.0","end")[:-1]
    T = preptext(T)
        
    return T

# Encrypt function
def enc(): 

    K = keysets()
    T = gettext()
    
    ctext.delete("1.0","end")
    
    # Try decrypting
    try:
        tx = enigma(T,K,decode=False)
    except Exception as e:
        ctext.insert("insert",str(e)) 
    
    ctext.insert("insert",tx)
         
# Decrypt function 
def dec(): 

    K = keysets()
    T = gettext()
    
    ctext.delete("1.0","end")
    
    # Try decrypting
    try:
        tx = enigma(T,K,decode=True)
    except Exception as e:
        ctext.insert("insert",str(e)) 
    
    ctext.insert("insert",tx)
    
# Randomize Key Settings
def randomize():
    
    C = ["I","II","III","IV","V"]
    random.shuffle(C)
    R = ["A","B","C"]
    
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    
    ciphers = ",".join(C[:3])
    reflect = random.choice(R)
    indexes = ",".join(I)
    
    ind1 = "".join(random.choices(alpha,k=5))
    ind2 = "".join(random.choices(alpha,k=5))
    ind3 = "".join(random.choices(nums,k=5))
    
    cipherRotors.delete("1.0","end")
    controlRotors.delete("1.0","end")
    indexRotors.delete("1.0","end")
    indicator.delete("1.0","end")
    controlPos.delete("1.0","end")
    indexPos.delete("1.0","end")
    
    cipherRotors.insert("insert",ciphers)
    controlRotors.insert("insert",controls)
    indexRotors.insert("insert",indexes)
    indicator.insert("insert",ind1)
    controlPos.insert("insert",ind2)
    indexPos.insert("insert",ind3)
    

# Button to run cipher in encrypt mode
encryptbutton = tk.Button(root, text="Encrypt", command = enc,
                          bg = 'lightblue', font = ('arial',14,'bold'))

# Button to run cipher in decrypt mode
decryptbutton = tk.Button(root, text="Decrypt", command = dec,
                          bg = 'lightgreen', font = ('arial',14,'bold'))


resetbutton = tk.Button(root, text="Clear", command = Reset, 
                       bg = 'lightslateblue', font = ('arial',14,'bold'))


# Button to run cipher in decrypt mode
exitbutton = tk.Button(root, text="Exit", command = qExit, 
                       bg = 'salmon', font = ('arial',14,'bold'))


# Button to randomize key settings
randombutton = tk.Button(root, text="Random\nSettings", command = randomize, 
                       bg = 'orange', font = ('arial',10))

# Labels
ptextLab = tk.Label(root,text="Input:",font = ('arial',14))
ctextLab = tk.Label(root,text="Output:",font = ('arial',14))
explainLab1 = tk.Label(root,
                      text="Plaintext can only include letters and spaces.",
                      font = ('arial',12),
                      wraplength=220,
                      relief=tk.GROOVE,
                      padx = 10, pady = 10)

explainLab2 = tk.Label(root,
                      text="Cipher and Control Rotors must be five roman numerals between one and ten.\n\nIndex Rotors must be five roman numerals between one and five.",
                      font = ('arial',12),
                      wraplength=220,
                      relief=tk.GROOVE,
                      padx = 10, pady = 10)

cipherLab =  tk.Label(root,text=" Cipher Settings",font = ('arial',10))
controlLab = tk.Label(root,text="Control Settings",font = ('arial',10))
indexLab =   tk.Label(root,text="  Index Settings",font = ('arial',10))
rotorLab =   tk.Label(root,text="Rotors",font = ('arial',10))
indicatorLab =  tk.Label(root,text="Indicators",font = ('arial',10))


# Tab control
ptext.bind("<Tab>", focus_next_widget)
cipherRotors.bind("<Tab>", focus_next_widget)
indicator.bind("<Tab>", focus_next_widget)
controlRotors.bind("<Tab>", focus_next_widget)
controlPos.bind("<Tab>", focus_next_widget)
indexRotors.bind("<Tab>", focus_next_widget)
indexPos.bind("<Tab>", focus_next_widget)
ctext.bind("<Tab>", focus_next_widget)



# Put everything in position
explainLab1.place(x=550,y=120)
explainLab2.place(x=550,y=200)

ptext.place(x=150,y=30)
ptextLab.place(x=60,y=30)

# Setting Labels
cipherLab.place(x=45,y=190)
controlLab.place(x=45,y=220)
indexLab.place(x=45,y=250)

rotorLab.place(x=150,y=165)
indicatorLab.place(x=330,y=165)

# Setting inputs
cipherRotors.place(x=150,y=190)
indicator.place(x=330,y=190)

controlRotors.place(x=150,y=220)
controlPos.place(x=330,y=220)

indexRotors.place(x=150,y=250)
indexPos.place(x=330,y=250)

# Buttons
encryptbutton.place(x=150,y=290)
decryptbutton.place(x=250,y=290)
resetbutton.place(x=400,y=290)
randombutton.place(x=430,y=190)

ctext.place(x=150,y=350)
ctextLab.place(x=50,y=350)

exitbutton.place(x=150,y=500)

randomize()

root.mainloop()
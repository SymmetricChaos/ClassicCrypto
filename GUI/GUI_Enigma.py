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
root.title("Enigma Emulator")

# Textboxes
ptext = tk.Text(root,height=8,width=40)

reflector = tk.Text(root,height=1,width=3)
rotors = tk.Text(root,height=1,width=10)
positions = tk.Text(root,height=1,width=4)
plugboard = tk.Text(root,height=1,width=20)
ringsets = tk.Text(root,height=1,width=4)

ctext = tk.Text(root,height=8,width=40)

# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.delete("1.0","end")
    ptext.delete("1.0","end")
    reflector.delete("1.0","end")
    rotors.delete("1.0","end")
    positions.delete("1.0","end")
    plugboard.delete("1.0","end")
    ringsets.delete("1.0","end")

# Move between widgets
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")


# Get the key settings
def keysets():

    k1 = rotors.get("1.0","end")[:-1]
    k2 = reflector.get("1.0","end")[:-1]
    k3 = positions.get("1.0","end")[:-1]
    k4 = plugboard.get("1.0","end")[:-1]
    k5 = ringsets.get("1.0","end")[:-1]
    
    k1 = k1.replace(" ","")
    k1 = k1.split(",")
    
    k4 = k4.replace(" ","")
    k4 = k4.split(",")
    
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
    print(K)
    ctext.delete("1.0","end")
    
    # Try decrypting
    try:
        tx = enigma(T,K,decode=False)
        ctext.insert("insert",tx)
    except Exception as e:
        ctext.insert("insert",str(e)) 


# Decrypt function 
def dec(): 

    K = keysets()
    T = gettext()
    
    ctext.delete("1.0","end")
    
    # Try decrypting
    try:
        tx = enigma(T,K,decode=True)
        ctext.insert("insert",tx)
    except Exception as e:
        ctext.insert("insert",str(e)) 


# Randomize Key Settings
def randomize():
    
    C = ["I","II","III","IV","V"]
    random.shuffle(C)
    R = ["A","B","C"]
    
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alpha)
    
    plugs = ["".join(alpha[:2]),
             "".join(alpha[2:4]),
             "".join(alpha[4:6]),
             "".join(alpha[6:8]),
             "".join(alpha[8:10]),
             "".join(alpha[10:12])]
    
    k1 = ",".join(C[:3])
    k2 = random.choice(R)
    k3 = "".join(random.choices(alpha,k=3))
    k4 = "".join(random.choices(alpha,k=3))
    k5 = ",".join(plugs)
    
    reflector.delete("1.0","end")
    rotors.delete("1.0","end")
    positions.delete("1.0","end")
    ringsets.delete("1.0","end")
    plugboard.delete("1.0","end")
    
    
    reflector.insert("insert",k2)
    rotors.insert("insert",k1)
    positions.insert("insert",k3)
    ringsets.insert("insert",k4)
    plugboard.insert("insert",k5)
    
    

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
                      text="Plaintext can only include letters.",
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



# Tab control
ptext.bind("<Tab>", focus_next_widget)

ctext.bind("<Tab>", focus_next_widget)


reflector.delete("1.0","end")
rotors.delete("1.0","end")
positions.delete("1.0","end")
ringsets.delete("1.0","end")
plugboard.delete("1.0","end")

# Put everything in position
explainLab1.place(x=550,y=120)
explainLab2.place(x=550,y=200)

ptext.place(x=150,y=30)
ptextLab.place(x=60,y=30)

# Setting Labels


# Setting inputs
reflector.place(x=150,y=190)
rotors.place(x=185,y=190)
positions.place(x=275,y=190)
plugboard.place(x=150,y=220)
ringsets.place(x=150,y=250)

# Buttons
encryptbutton.place(x=150,y=290)
decryptbutton.place(x=250,y=290)
resetbutton.place(x=400,y=290)
randombutton.place(x=400,y=190)

ctext.place(x=150,y=350)
ctextLab.place(x=50,y=350)

exitbutton.place(x=150,y=500)

randomize()

root.mainloop()
import tkinter as tk
import random
from Ciphers.Enigma import enigma
from Ciphers.UtilityFunctions import preptext

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,700)
root.minsize(800,700)

# Title of the window
root.title("Enigma Emulator")

# Textboxes
ptext = tk.Text(root,height=8,width=40)

reflector = tk.Text(root,height=1,width=3)
positions = tk.Text(root,height=1,width=4)
plugboard = tk.Text(root,height=1,width=20)
ringsets = tk.Text(root,height=1,width=4)

ctext = tk.Text(root,height=8,width=40)

RE = tk.StringVar()
RE.set(0)
reflectG = []
for i,j in zip(["A","B","C"],[0,1,2]):
    reflectG.append(tk.Radiobutton(root, text = i, variable = RE, value = j) )

R1 = tk.StringVar()
R1.set(0)
rotorG1 = []
for i,j in zip(["I","II","III","IV","V"],[0,1,2,3,4]):
    rotorG1.append(tk.Radiobutton(root, text = i, variable = R1, value = j) )

R2 = tk.StringVar()
R2.set(1)
rotorG2 = []
for i,j in zip(["I","II","III","IV","V"],[0,1,2,3,4]):
    rotorG2.append(tk.Radiobutton(root, text = i, variable = R2, value = j) )

R3 = tk.StringVar()
R3.set(2)
rotorG3 = []
for i,j in zip(["I","II","III","IV","V"],[0,1,2,3,4]):
    rotorG3.append(tk.Radiobutton(root, text = i, variable = R3, value = j) )


# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.delete("1.0","end")
    ptext.delete("1.0","end")
    reflector.delete("1.0","end")
    positions.delete("1.0","end")
    plugboard.delete("1.0","end")
    ringsets.delete("1.0","end")

# Move between widgets
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")


# Get the key settings
def keysets():

    rtrL = ["I","II","III","IV","V"]
    
    RG = [R1.get(), R2.get(), R3.get()]
    k1 = [rtrL[int(i)] for i in RG]
    
    k2 = reflector.get("1.0","end")[:-1]
    k3 = positions.get("1.0","end")[:-1]
    k4 = plugboard.get("1.0","end")[:-1]
    k5 = ringsets.get("1.0","end")[:-1]
    
    
    k4 = k4.replace(" ","")
    k4 = k4.split(",")
    
    return [k1,k2,k3,k4,k5]


# Get the text from the ptext box and prepare it
def gettext():
    T = ptext.get("1.0","end")[:-1]
    T = preptext(T,silent=True)
        
    return T

# Encrypt function
def enc(): 

    K = keysets()
    T = gettext()
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
    
    rtr = list("01234")
    random.shuffle(rtr)
    for radio,pos in zip([R1,R2,R3],rtr[:3]):
        radio.set(pos)
    
    RE.set(random.randint(0,2))
    
    
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alpha)
    
    plugs = ["".join(alpha[:2]),
             "".join(alpha[2:4]),
             "".join(alpha[4:6]),
             "".join(alpha[6:8]),
             "".join(alpha[8:10]),
             "".join(alpha[10:12])]
    
    k3 = "".join(random.choices(alpha,k=3))
    k4 = "".join(random.choices(alpha,k=3))
    k5 = ",".join(plugs)
    
    positions.delete("1.0","end")
    ringsets.delete("1.0","end")
    plugboard.delete("1.0","end")
    
    
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

rotorLab = tk.Label(root,
                      text="Reflector and Rotors",
                      font = ('arial',10))

ringLab = tk.Label(root,
                      text="Rings",
                      font = ('arial',10))

plugLab = tk.Label(root,
                      text="Plugs",
                      font = ('arial',10))

offsetLab = tk.Label(root,
                      text="Offsets",
                      font = ('arial',10))

# Tab control
ptext.bind("<Tab>", focus_next_widget)

ctext.bind("<Tab>", focus_next_widget)


# Put everything in position


ptext.place(x=150,y=30)
ptextLab.place(x=60,y=30)

# Setting Labels
plugLab.place(x=100,y=300)
ringLab.place(x=100,y=360)
offsetLab.place(x=330,y=170)

explainLab1.place(x=550,y=120)
explainLab2.place(x=550,y=200)
rotorLab.place(x=150,y=170)

# Setting inputs
for x,rg in enumerate([reflectG,rotorG1,rotorG2,rotorG3]):
    for y,button in enumerate(rg):
        button.place(x=150+x*45,y=190+y*20)

positions.place(x=335,y=195)
ringsets.place(x=150,y=360)
plugboard.place(x=150,y=300)

# Buttons
buttonRow = 390
encryptbutton.place(x=150,y=buttonRow)
decryptbutton.place(x=250,y=buttonRow)
resetbutton.place(x=400,y=buttonRow)

randombutton.place(x=400,y=190)

ctext.place(x=150,y=450)
ctextLab.place(x=50,y=450)

exitbutton.place(x=150,y=580)

randomize()

root.mainloop()
import tkinter as tk
import random
from Ciphers.SIGABA import SIGABA


# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("SIGABA Emulator")

# Textboxes
ptext = tk.Text(root,height=8,width=40)

cipherRotors = tk.Text(root,height=1,width=20)
indicator =  tk.Text(root,height=1,width=8)
controlRotors = tk.Text(root,height=1,width=20)
controlPos = tk.Text(root,height=1,width=8)
indexRotors = tk.Text(root,height=1,width=20)
indexPos =   tk.Text(root,height=1,width=8)

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

    k1 = cipherRotors.get("1.0","end")[:-1]
    k2 = controlRotors.get("1.0","end")[:-1]
    k3 = indexRotors.get("1.0","end")[:-1]
    
    k1 = k1.replace(" ","")
    k1 = k1.split(",")
    
        
    k2 = k2.replace(" ","")
    k2 = k2.split(",")
        
    k3 = k3.replace(" ","")
    k3 = k3.split(",")
    
    
    k4 = indicator.get("1.0","end")[:-1]
    k5 = controlPos.get("1.0","end")[:-1]
    k6 = indexPos.get("1.0","end")[:-1]
    
    return [k1,k2,k3,k4,k5,k6]


# Get the text from the ptext box and prepare it
def gettext():
    T = ptext.get("1.0","end")[:-1]
    T = T.upper()
    
    for i in T:
        if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            ctext.insert("insert","Letters and spaces only.")
            break
    
    return T

# Encrypt function
def enc(): 

    K = keysets()
    T = gettext()
    
    ctext.delete("1.0","end")
    
    # Try decrypting
    try:
        tx = SIGABA(T,K,decode=False)
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
        tx = SIGABA(T,K,decode=True)
    except Exception as e:
        ctext.insert("insert",str(e)) 
    
    ctext.insert("insert",tx)
    
# Randomize Key Settings
def randomize():
    
    C = ["I","II","III","IV","V","VI","VII","VIII","IX","X"]
    I = ["I","II","III","IV","V"]
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    nums = list("0123456789")
    random.shuffle(C)
    random.shuffle(I)
    
    ciphers = ",".join(C[:5])
    controls = ",".join(C[5:])
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
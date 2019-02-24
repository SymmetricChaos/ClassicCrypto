import tkinter as tk
from Attacks.SubstitutionCracker import substitutionCracker
from Ciphers.UtilityFunctions import saveFormat, restoreFormat

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("Substitution Cipher Cracker")

# Two textboxes
ctext = tk.Text(root,height=10,width=50)
ptext = tk.Text(root,height=10,width=50)

rounds = tk.Text(root,height=1,width=5)
rounds.insert("insert","10")
# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    ctext.delete("1.0","end")
    ptext.delete("1.0","end")
  

# Encrypt function
def crackIt(): 

    # Get the text from the ptext box
    T = ctext.get("1.0","end")[:-1]
    T, pos, char,case = saveFormat(T)

    R = int(rounds.get("1.0","end")[:-1])

    tx = substitutionCracker(T,R)

    # Blank the ctext box then put the text in it
    ptext.delete("1.0","end")
    ptext.insert("insert",restoreFormat(tx, pos, char,case))
  
# Button to run cipher in encrypt mode
crackbutton = tk.Button(root, text="Solve", command = crackIt,
                          bg = 'lightblue', font = ('arial',14,'bold'))

resetbutton = tk.Button(root, text="Reset", command = Reset, 
                       bg = 'lightslateblue', font = ('arial',14,'bold'))


# Button to run cipher in decrypt mode
exitbutton = tk.Button(root, text="Exit", command = qExit, 
                       bg = 'salmon', font = ('arial',14,'bold'))


# Labels
ptextLab = tk.Label(root,text="Plaintext:",font = ('arial',14))
ctextLab = tk.Label(root,text="Ciphertext:",font = ('arial',14))

describe = tk.Label(root,text="You may have to run the program multiple times.",
                    font = ('arial',12),
                    wraplength=200,
                    relief=tk.GROOVE,
                    padx = 10, pady = 10)

# Put everything in position
ctext.place(x=150,y=30)
ctextLab.place(x=40,y=30)

rounds.place(x=570,y=40)

crackbutton.place(x=150,y=210)
resetbutton.place(x=250,y=210)

describe.place(x=570,y=75)

ptext.place(x=150,y=260)
ptextLab.place(x=50,y=260)

exitbutton.place(x=150,y=440)

root.mainloop()
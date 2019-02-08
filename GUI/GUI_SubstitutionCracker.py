import tkinter as tk
from Attacks.SubstitutionCracker import substitutionCracker


# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("Crack Substitution")

# Two textboxes
ctext = tk.Text(root,height=6,width=60)
ptext = tk.Text(root,height=6,width=60)

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
  
    # Blank the ctext box then put the text in it
    ptext.delete("1.0","end")
    ptext.insert("insert",substitutionCracker(T,10)) 

  
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

# But everything in position

ctext.place(x=150,y=30)
ctextLab.place(x=40,y=30)


crackbutton.place(x=150,y=160)
resetbutton.place(x=400,y=160)

ptext.place(x=150,y=220)
ptextLab.place(x=50,y=220)

exitbutton.place(x=150,y=320)

root.mainloop()
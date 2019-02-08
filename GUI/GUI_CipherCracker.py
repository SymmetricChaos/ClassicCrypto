import tkinter as tk
from Attacks.SubstitutionCracker import substitutionCracker
from Attacks.AutokeyCracker import autokeyCracker

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

# Title of the window
root.title("Cipher Crackers")

# Two textboxes
ctext = tk.Text(root,height=7,width=60)
ptext = tk.Text(root,height=7,width=60)

# Dropdown Menu
setting = tk.StringVar(root)
setting.set("choose a cipher")
settingMenu = tk.OptionMenu(root,setting,"substitution","autokey")


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

    S = setting.get()
    
    # We use a dictionary as basically a as a switch statement
    # They keys are the names of the cipher while the values are the cipher
    # functions that we imported
    settingDict = {"autokey": autokeyCracker,
                  "substitution": substitutionCracker}

    # Blank the ctext box then put the text in it
    ptext.delete("1.0","end")
    ptext.insert("insert",settingDict[S](T,10)) 

  
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

# Put everything in position
settingMenu.place(x=650,y=30)

ctext.place(x=150,y=30)
ctextLab.place(x=40,y=30)


crackbutton.place(x=150,y=160)
resetbutton.place(x=250,y=160)

ptext.place(x=150,y=220)
ptextLab.place(x=50,y=220)

exitbutton.place(x=150,y=400)

root.mainloop()
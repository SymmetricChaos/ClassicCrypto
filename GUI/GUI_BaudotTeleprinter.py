import tkinter as tk
from itertools import product
from Codes import baudot

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(900,600)
root.minsize(900,600)

# Title of the window
root.title("Baudot Teleprinter")

# One textboxes
outtext = tk.Text(root,height=25,width=40)

# Exit Button
def qExit(): 
    root.destroy() 

# Reset Button
def Reset(): 
    outtext.delete("1.0","end")




resetbutton = tk.Button(root, text="Reset", command = Reset, 
                       bg = 'lightslateblue', font = ('arial',14,'bold'))


# Button to run cipher in decrypt mode
exitbutton = tk.Button(root, text="Exit", command = qExit, 
                       bg = 'salmon', font = ('arial',14,'bold'))


# Labels
ptextLab = tk.Label(root,text="Input:",font = ('arial',14))

# Put everything in position
L = list("QWERTYUIOPASDFGHJKLZXCVBNM*a&<>_")
for y,x in product(range(4),range(8)):
    bt = tk.Button(root, text=L.pop(0), command = Reset, 
                       bg = 'lightslateblue', font = ('arial',14,'bold'))
    bt.place( x = 420+x*50, y = 50+y*50 )
    bt.config(width=2, height=1)

outtext.place(x=50,y=30)

resetbutton.place(x=55,y=450)

exitbutton.place(x=150,y=450)

root.mainloop()
import tkinter as tk

from Codes import baudot

# Create the window
root = tk.Tk()

# Don't let the user change the window size
root.maxsize(800,600)
root.minsize(800,600)

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

B = []
for i in range(32):
    B.append( tk.Button(root, text=str(i), command = Reset, 
                       bg = 'lightslateblue', font = ('arial',14,'bold')) )

fr = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)

resetbutton = tk.Button(root, text="Reset", command = Reset, 
                       bg = 'lightslateblue', font = ('arial',14,'bold'))


# Button to run cipher in decrypt mode
exitbutton = tk.Button(root, text="Exit", command = qExit, 
                       bg = 'salmon', font = ('arial',14,'bold'))


# Labels
ptextLab = tk.Label(root,text="Input:",font = ('arial',14))

# Put everything in position
fr.place(x=200,y=30)

outtext.place(x=50,y=30)

resetbutton.place(x=55,y=450)

exitbutton.place(x=150,y=450)

root.mainloop()
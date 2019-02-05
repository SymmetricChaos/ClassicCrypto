# import tkinter module 
from tkinter import Tk, Frame, SUNKEN, TOP, LEFT, Label, StringVar, Entry, Button
  
from Ciphers.Vigenere import vigenere

# creating root object 
root = Tk() 
  
# defining size of window 
root.geometry("1100x500")
root.resizable(0,0)
  
# setting up the title of window 
root.title("Message Encryption and Decryption") 
  
Tops = Frame(root, width = 1100, relief = SUNKEN) 
Tops.pack(side = TOP) 
  
f1 = Frame(root, width = 1100, height = 500, 
                            relief = SUNKEN) 
f1.pack(side = LEFT) 


lblInfo = Label(Tops, font = ('helvetica', 20, 'bold'), 
          text = "Vigenère cipher", 
                     fg = "Black", bd = 10, anchor='w') 
                       

lblInfo.grid(row = 1, column = 0) 
  
Msg = StringVar() 
key = StringVar() 
Result = StringVar() 
  
# exit function 
def qExit(): 
    root.destroy() 
  
# Function to reset the window 
def Reset():
    Msg.set("") 
    key.set("") 
    Result.set("") 
  
  

# labels 
lblMsg = Label(f1, font = ('arial', 16, 'bold'), 
         text = "MESSAGE", bd = 16, anchor = "w") 
           
lblMsg.grid(row = 0, column = 1) 
  
txtMsg = Entry(f1, font = ('arial', 16, 'bold'), 
         textvariable = Msg, bd = 10, insertwidth = 4, 
                bg = "powder blue", justify = 'right') 
                  
txtMsg.grid(row = 0, column = 2) 
  
lblkey = Label(f1, font = ('arial', 16, 'bold'), 
            text = "KEY", bd = 16, anchor = "w") 
              
lblkey.grid(row = 1, column = 1) 
  
txtkey = Entry(f1, font = ('arial', 16, 'bold'), 
         textvariable = key, bd = 10, insertwidth = 4, 
                bg = "powder blue", justify = 'right') 
                  
txtkey.grid(row = 1, column = 2) 
  
lblService = Label(f1, font = ('arial', 16, 'bold'), 
             text = "RESULT", bd = 16, anchor = "w") 
               
lblService.grid(row = 2, column = 1) 
  
txtService = Entry(f1, font = ('arial', 16, 'bold'),  
             textvariable = Result, bd = 10, insertwidth = 4, 
                       bg = "powder blue", justify = 'right') 
                         
txtService.grid(row = 2, column = 2) 
  
# Encrypt
def enc(): 

    clear = Msg.get() 
    k = key.get() 
  
    Result.set(vigenere(clear,k,decode=True)) 

# Decrypt       
def dec(): 

    clear = Msg.get() 
    k = key.get() 
    Result.set(vigenere(clear,k,decode=False)) 
  
  
# Show message button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                       text = "Encrypt", bg = "powder blue", 
                         command = enc).grid(row = 7, column = 1) 

# Show message button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                       text = "Decrypt", bg = "powder blue", 
                         command = dec).grid(row = 7, column = 2) 
  

# Reset button 
btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
                  fg = "black", font = ('arial', 16, 'bold'), 
                    width = 10, text = "Reset", bg = "green", 
                   command = Reset).grid(row = 7, column = 3) 
  
# Exit button 
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,  
                 fg = "black", font = ('arial', 16, 'bold'), 
                      width = 10, text = "Exit", bg = "red", 
                  command = qExit).grid(row = 8, column = 3) 
  
# keeps window alive 
root.mainloop() 
import os
import pyAesCrypt
from tkinter import *

def crypt():
    filetocrp = txt.get()
    password = txt1.get()
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(str(filetocrp), str(filetocrp) + ".crp", password, bufferSize)
    os.remove(filetocrp)

def decrypt():
    filetocrp = txt.get()
    password = txt1.get()
    bufferSize = 512*1024
    pyAesCrypt.decryptFile(str(filetocrp), str(os.path.splitext(filetocrp)[0]), password, bufferSize)
    os.remove(filetocrp)

window = Tk()
window.title("FileCrypter v 1.0")

lbl = Label(text = "Welcome!")
lbl.grid(column = 0, row = 1)

lbl1 = Label(text = "Input File: ")
lbl1.grid(column = 0, row = 3)

lbl2 = Label(text = "Input Password: ")
lbl2.grid(column = 0, row = 4)

lbl3 = Label(text = "")
lbl3.grid(column = 0, row = 6)

txt = Entry(window, width=20)
txt.grid(column = 1, row = 3 )

txt1 = Entry(window, width=20)
txt1.grid(column = 1, row = 4 )

btn = Button(window, text = "Crypt", command=crypt, width = 10)
btn.grid(column= 1, row = 7)

btn = Button(window, text = "DeCrypt", command=decrypt, width = 10)
btn.grid(column= 1, row = 9)

window.geometry('400x250')
window.mainloop()


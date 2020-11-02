import tkinter
from tkinter import *

root = Tk()

text = Label (root, text="hello world  hhhhhhhhhhhhhhhhhhhhhhhhvvffffffffffffffffffrutktfttjtj")
text.pack()

root.mainloop()
from tkinter import messagebox

def hejsan():
    messagebox.showinfo("hejsan", "hallå, hallå")
root2 = Tk()
root2.geometry(200*200)
text= Label (root2, text="hello world")

text.pack()

knapp1 = Button(root2, text="säg hej!")
knapp1.pack()

knapp2=Button(root2,text="hejdå")
knapp2.pack()

root2.mainloop()
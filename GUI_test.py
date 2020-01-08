import tkinter
from tkinter import *

root = Tk()

e = Entry(root, width=50)
txt = Text(root)
txt.tag_config('warning', background="yellow", foreground="red")
e.insert(0, "txt")
def click():
    myLable = Label(root, text=e.get()).pack()



label1 = Label(root, text="hello")
label2 = Label(root, text="bye")
label3 = Label(root, text="morning")
button1 = Button(root, text="Button1", padx=50, command=click, highlightbackground="Red", fg="Blue")

e.pack()
button1.pack()


root.mainloop()

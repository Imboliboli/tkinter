import tkinter as tk
from tkinter import *

root = Tk()
root.title("Simple Calculator")
num = 0

list_1 = []
list_2 = []


def click(number):
    size = len(e.get())
    # fist element cannot be a non digit
    if (size == 0 and (number.isdigit() == False)) or (
            size != 0 and (e.get()[-1].isdigit() == False and number.isdigit() == False)):
        print("cant do it")

    else:
        e.insert(END, number)


def clear():
    e.delete(0, END)


def ans():
    temp = e.get().split("+")
    ans =0
    try:

        for x in range(len(temp)):
             ans+=int(temp[x])
        clear()
        e.insert(0, ans)
    except:
        print("nope")




e = tk.Entry(root, text=num, width=15, borderwidth=3, relief="groove", font=('Arial', 40))
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

button_1 = tk.Button(root, text="1", padx=45, pady=10, command=lambda: click("1")).grid(row=3, column=0, pady=5)
button_2 = tk.Button(root, text="2", padx=45, pady=10, command=lambda: click("2")).grid(row=3, column=1, pady=5)
button_3 = tk.Button(root, text="3", padx=45, pady=10, command=lambda: click("3")).grid(row=3, column=2, pady=5)
button_4 = tk.Button(root, text="4", padx=45, pady=10, command=lambda: click("4")).grid(row=2, column=0, pady=5)
button_5 = tk.Button(root, text="5", padx=45, pady=10, command=lambda: click("5")).grid(row=2, column=1, pady=5)
button_6 = tk.Button(root, text="6", padx=45, pady=10, command=lambda: click("6")).grid(row=2, column=2, pady=5)
button_7 = tk.Button(root, text="7", padx=45, pady=10, command=lambda: click("7")).grid(row=1, column=0, pady=5)
button_8 = tk.Button(root, text="8", padx=45, pady=10, command=lambda: click("8")).grid(row=1, column=1, pady=5)
button_9 = tk.Button(root, text="9", padx=45, pady=10, command=lambda: click("9")).grid(row=1, column=2, pady=5)
button_0 = tk.Button(root, text="0", padx=110, pady=10, command=lambda: click("0")).grid(row=4, column=0, padx=5,
                                                                                         pady=5,
                                                                                         columnspan=2)
button_decimal = tk.Button(root, text=".", padx=45, pady=10, command=lambda: click(".")).grid(row=4, column=2, pady=5)
button_add = tk.Button(root, text="+", padx=45, pady=10, command=lambda: click("+")).grid(row=4, column=3, pady=5)
button_equal = tk.Button(root, text="=", padx=45, pady=10, command=lambda: ans()).grid(row=3, column=3, pady=5)
button_clear = tk.Button(root, text="AC", padx=45, pady=10, command=lambda: clear()).grid(row=1, column=3, pady=5)

root.mainloop()

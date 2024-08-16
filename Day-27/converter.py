import tkinter
from tkinter import *


def calculate():
    try:
        value = float(input_box.get())
        value *= 1.609
        label_3.config(text=value)
    except ValueError:
        print("Invalid Input.")


window = Tk()
window.title("Mile to KM Converter.")
window.minsize(width=300, height=100)

input_box = Entry()
input_box.grid(row=0, column=1)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="Equals to")
label_2.grid(row=1, column=0)

label_3 = Label(text="0")
label_3.grid(row=1, column=1)

label_4 = Label(text="Kilometers")
label_4.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()

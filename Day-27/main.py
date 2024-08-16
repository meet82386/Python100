import random
import tkinter

window = tkinter.Tk()

window.title("My first Tkinter GUI program.")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="Meet Thummar", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "My New Label"
my_label.config(text="Another new label.")

# Buttons

data = [
    "Republic of India",
    "Islamic Republic of Pakistan",
    "People's Republic of China",
    "United Status of America",
    "United Kingdom"
]


def print_will_do_nothing():
    my_label.config(text=random.choice(data))


button = tkinter.Button(text="Click to show random name.", command=print_will_do_nothing)
button.pack()

# Entry

entry = tkinter.Entry()
entry.pack()


def print_value():
    value = entry.get()
    data.append(value)
    my_label.config(text=value)
    entry.delete(0, tkinter.END)
    entry.insert(0, "")


button_2 = tkinter.Button(text="Click to show entered value.", command=print_value)
button_2.pack()


# Text box
text_box = tkinter.Text(height=5, width=40)
text_box.pack()

# SpinBox
spinbox = tkinter.Spinbox()
spinbox.pack()

window.mainloop()

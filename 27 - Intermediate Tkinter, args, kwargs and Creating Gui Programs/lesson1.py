import turtle
import tkinter

window = tkinter.Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_event():
    print("clicked")
    my_label.config(text="clicked")
    my_label.config(text=input.get())


# Label

my_label = tkinter.Label(text="Hello there label",
                         font=('Arial', 24, "italic"))


my_label["text"] = "New text"  # I can change like this
my_label.config(text="new text 2")  # or like this

my_label.grid(column=0, row=0)

# Button


button = tkinter.Button(text="Click me", command=button_event)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="new button")
new_button.grid(column=3, row=2)

# Enrty

input = tkinter.Entry(width=10)
input.grid(column=2, row=0)


window.mainloop()

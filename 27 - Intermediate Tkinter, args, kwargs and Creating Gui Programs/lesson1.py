import turtle
import tkinter

window = tkinter.Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)


# Label

my_label = tkinter.Label(text="Hello there label",
                         font=('Arial', 24, "italic"))
my_label.pack()

my_label["text"] = "New text"  # I can change like this
my_label.config(text="new text 2")  # or like this

# Button


def button_event():
    print("clicked")
    my_label.config(text="clicked")
    my_label.config(text=input.get())


button = tkinter.Button(text="Click me", command=button_event)
button.pack()

# Enrty

input = tkinter.Entry(width=50)
input.pack()


window.mainloop()

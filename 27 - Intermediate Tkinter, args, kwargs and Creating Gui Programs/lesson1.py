import turtle
import tkinter

window = tkinter.Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)


# Label

my_label = tkinter.Label(text="Hello there label",
                         font=('Arial', 24, "italic"))
my_label.pack(side="left")


window.mainloop()

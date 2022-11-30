import tkinter

window = tkinter.Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


def calculater():
    user_input = input.get()
    km = int(user_input) * 1.609
    return label_result.config(text=km)


# Enrty

input = tkinter.Entry()
input.grid(column=1, row=0)

label_mile = tkinter.Label(text="Miles")
label_mile.grid(column=2, row=0)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = tkinter.Label()
label_result.grid(column=1, row=1)

label_km = tkinter.Label(text="Km")
label_km.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=calculater)
button.grid(column=1, row=2)


window.mainloop()

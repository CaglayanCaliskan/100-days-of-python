from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(bg="white", padx=100, pady=100)


canvas = Canvas(width=200, height=189, bg="white", border=2)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=tomato_img)
canvas.grid(column=1, row=0, columnspan=2)

# Static titles
label_website = Label(text="Website:", bg="white", pady=10)
label_website.grid(column=0, row=3)

label_email = Label(text="Email/Username:", bg="white", pady=10)
label_email.grid(column=0, row=4)

label_password = Label(text="Password:", bg="white", pady=10)
label_password.grid(column=0, row=5)

# Inputs
entry_website = Entry(width=60, border=2)
entry_website.grid(column=1, row=3, columnspan=2)

entry_email = Entry(width=60, border=2)
entry_email.grid(column=1, row=4, columnspan=2)

entry_password = Entry(border=2, width=40)
entry_password.grid(column=1, row=5)

# Buttons
button_generate = Button(text="Generate Password",
                         border=1, bg="#FC2E20", fg="white")
button_generate.grid(column=2, row=5)

button_add = Button(text="Add", bg="#FD7F20", fg="white").grid(
    column=1, columnspan=2, row=6, sticky="we")

window.mainloop()

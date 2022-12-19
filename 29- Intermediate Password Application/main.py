import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    password = ""
    for _ in range(4):
        list = [random.choice(printable) for i in range(4)]
        block = "".join(list)
        if _ == 3:
            password += block
        else:
            password += block + "-"
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showerror(title=f"Oops",
                             message="please fill blanks")
    else:
        is_ok = messagebox.askokcancel(
            title="Comfirm", message=f"These are the derails entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save? ")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                entry_email.delete(0, END)
                entry_email.insert(0, "SAVED to File")
                entry_website.delete(0, END)
                entry_website.insert(0, "SAVED to File")

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(
            title="404 Not Found", message=f"No Data File exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="404 Not Found", message=f"Not found any password,Please try another input")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(bg="white", padx=40, pady=50)


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

# Static titles
label_website = Label(text="Website:", bg="white", pady=10)
label_website.grid(column=0, row=3)

label_email = Label(text="Email/Username:", bg="white", pady=10)
label_email.grid(column=0, row=4)

label_password = Label(text="Password:", bg="white", pady=10)
label_password.grid(column=0, row=5)

# Inputs
entry_website = Entry(border=2, width=32)
entry_website.grid(column=1, row=3)
entry_website.focus()

entry_email = Entry(border=2, width=50)
entry_email.grid(column=1, row=4, columnspan=2)
entry_email.insert(0, "example@gmail.com")

entry_password = Entry(border=2, width=32)
entry_password.grid(column=1, row=5)

# Buttons
button_search = Button(text="Search", border=1,
                       bg='#FC2E20', fg="white", width=14, command=find_password)
button_search.grid(column=2, row=3)

button_generate = Button(text="Generate Password",
                         border=1, bg="#FC2E20", fg="white", command=generator)
button_generate.grid(column=2, row=5)

button_add = Button(text="Add", bg="#FD7F20", fg="white", command=save_password).grid(
    column=1, columnspan=2, row=6, sticky="we")


window.mainloop()

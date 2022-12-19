from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv("./data/german500.csv")
to_learn = data.to_dict(orient="records")  # AMAZING


# ---------------------------- FUNCTİON ------------------------------- #


def next_card():
    current_card = random.choice(to_learn)
    print(current_card["Deutch"], current_card["Türkçe"])
    canvas.itemconfig(card_title, text="Deutch")
    canvas.itemconfig(card_word, text=current_card["Deutch"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
logo_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=logo_img)
card_title = canvas.create_text(
    400, 150, font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(
    400, 263, font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

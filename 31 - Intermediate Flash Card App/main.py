import time
from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv("./data/german500.csv")
to_learn = data.to_dict(orient="records")  # AMAZING


# ---------------------------- FUNCTİON ------------------------------- #
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Deutch", fill="black")
    canvas.itemconfig(card_word, text=current_card["Deutch"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    # timer()


def flip_card():
    canvas.itemconfig(card_title, text="Türkçe", fill="white")
    canvas.itemconfig(card_word, text=current_card["Türkçe"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# def timer():
#     count = 3
#     canvas.itemconfig(counter, text=count)
#     for t in range(count, 0, -1):
#         print(count)
#         count -= 1
#         time.sleep(1)
#         canvas.itemconfig(counter, text=count)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(
    400, 263, font=('Ariel', 60, 'bold'))
counter = canvas.create_text(700, 50, font=(
    'Ariel', 60, 'bold'), text="3", fill="green")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

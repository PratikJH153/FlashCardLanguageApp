from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

isFlipped = False
new_word = {}


def next_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(to_learn)
    text_canvas.itemconfig(language_label, text="French", fill="black")
    text_canvas.itemconfig(word_label, text=new_word['French'], fill="black")
    text_canvas.itemconfig(card_image, image=card_front_image)

    flip_timer = window.after(3000, flip_card)


def know_word():
    global to_learn
    to_learn.remove(new_word)


def unknown_word():
    pass


def flip_card():
    text_canvas.itemconfig(card_image, image=card_back_image)
    text_canvas.itemconfig(language_label, text="English", fill="white")
    text_canvas.itemconfig(word_label, text=new_word["English"], fill="white")


# --------------------------- UI SETUP ---------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

text_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = text_canvas.create_image(400, 263, image=card_front_image)
language_label = text_canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_label = text_canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
text_canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.config(borderwidth=0, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=next_card)
right_button.config(borderwidth=0, highlightthickness=0)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()

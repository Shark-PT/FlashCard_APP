from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card= {}



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card  =random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = language_text = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
card_word = word_text=canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0,command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()

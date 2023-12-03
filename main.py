from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")



def next_card():
    current_card  =random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card_img)
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

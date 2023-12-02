from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card_img)
language_text = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
word_text=canvas.create_text(400, 263, text="word", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)



window.mainloop()

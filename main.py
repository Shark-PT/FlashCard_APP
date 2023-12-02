from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR)

canvas = Canvas(width=500, height=500)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(100, 100, image=front_card_img)
timer_text = canvas.create_text(10, 10, text="French", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.pack()




window.mainloop()

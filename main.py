from tkinter import Tk
from tkinter import Canvas, PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

text_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
text_canvas.create_image(400, 263, image=card_back_image)
text_canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
text_canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))
text_canvas.grid(column=2, row=0, columnspan=4)


wrong_canvas = Canvas(width=100, height=99, highlightthickness=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_canvas.create_image(50, 49, image=wrong_image)
wrong_canvas.grid(column=3, row=1)

right_canvas = Canvas(width=100, height=100, highlightthickness=0)
right_image = PhotoImage(file="images/right.png")
right_canvas.create_image(50, 50, image=right_image)
right_canvas.grid(column=4, row=1)


window.mainloop()

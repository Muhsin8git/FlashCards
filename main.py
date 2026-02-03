import random
from tkinter import *
import pandas
import random

to_learn ={}
try:
    file =pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("./data/french_words.csv")
    to_learn = original_file.to_dict(orient="records")
else:
    to_learn = file.to_dict(orient="records")
current_card ={}
def next_card():
    global current_card,flip_timer
    current_card = random.choice(to_learn)
    french_word =current_card["French"]
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word, text=french_word,fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
def known():
    to_learn.remove(current_card)
    data =pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer =window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img =canvas.create_image(400,263,image=card_front_img)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_title =canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


cross_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_img,highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

check_img = PhotoImage(file="./images/right.png")
known_button =Button(image=check_img,highlightthickness=0,command=known)
known_button.grid(row=1,column=1)


next_card()


window.mainloop()
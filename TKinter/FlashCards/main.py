from tkinter import *
import pandas as pd
import random
flip = None
open_card = {}
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
def loard_csv():
    global dict_from_csv
    try:
        dict_from_csv = pd.read_csv('data\sp_to_learn.csv').to_dict(orient="records")
    except FileNotFoundError:
        dict_from_csv = pd.read_csv('data\spanish_words.csv').to_dict(orient="records")
    return dict_from_csv

word_dict = loard_csv()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=open_card["English"], fill="white")
    canvas.itemconfig(background, image=back)

def next_card():
    global open_card, flip
    if flip:
        window.after_cancel(flip)
    open_card = random.choice(word_dict)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=open_card["Spanish"], fill="black")
    canvas.itemconfig(background, image=front)
    flip = window.after(3000, flip_card)

def remove_card():
    dict_from_csv.remove(open_card)
    data = pd.DataFrame(dict_from_csv)
    data.to_csv("data\sp_to_learn.csv", index=False)
    next_card()


window = Tk()
front = PhotoImage(file="images\card_front.png")
back = PhotoImage(file="images\card_back.png")
window.title("Langash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background = canvas.create_image(400, 263, image=front)
card_title = canvas.create_text(400, 150, text="Spanish", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

nope = PhotoImage(file="images\wrong.png")
nope_button = Button(image=nope, highlightthickness=0, command=next_card)
nope_button.grid(column=0, row=1)

yup = PhotoImage(file="images\yep.png")
yup_button = Button(image=yup, highlightthickness=0, command=remove_card)
yup_button.grid(column=1, row=1)

next_card()

window.mainloop()
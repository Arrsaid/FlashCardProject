from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/french_words.csv")

data_dic = data.to_dict(orient="records")
word_dic = {}
# +---------------------- ANSWER -----------------------+


def right_answer():
    data_dic.remove(word_dic)
    data_to_learn = pandas.DataFrame(data_dic)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def next_word():
    global word_dic, flip_timer
    window.after_cancel(flip_timer)
    word_dic = random.choice(data_dic)
    canvas.itemconfig(canvas_text1, text="French", fill="black")
    canvas.itemconfig(canvas_text2, text=word_dic["French"], fill="black")
    canvas.itemconfig(image, image=front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_text1, text="English", fill="white")
    canvas.itemconfig(canvas_text2, text=word_dic["English"], fill="white")
    canvas.itemconfig(image, image=back_image)


# +--------------------- UI SETUP ----------------------+
window = Tk()
window.title("Flash Cards")
window.config(padx=80, pady=80, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_image)
canvas_text1 = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
canvas_text2 = canvas.create_text(400, 280, text="", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_answer)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

next_word()


window.mainloop()

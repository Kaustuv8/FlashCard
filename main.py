BACKGROUND_COLOR = "#B1DDC6"
import tkinter
import pandas as p
import random as r


def Word_Change():

    global Word, flip_timer
    Window.after_cancel(flip_timer)
    Word = r.choice(ToLearn)
    Canvas.itemconfig(FCardImage, image=Front_Card)
    Canvas.itemconfig(TitleText, text="French", fill="Black")
    Canvas.itemconfig(WordText, text=Word["French"], fill="Black")
    flip_timer = Window.after(3000, Word_To_English)


def Save():
    ToLearn.remove(Word)
    UpdateCsv()
    Word_Change()


def UpdateCsv():
    MissedWords = p.DataFrame(ToLearn)
    MissedWords.to_csv("./data/words_to_learn.csv", index=False)

def Word_To_English():
    global Word
    Canvas.itemconfig(FCardImage, image=Back_Card)
    Canvas.itemconfig(TitleText, text="English", fill="White")
    Canvas.itemconfig(WordText, text=Word["English"], fill = "White")
Window = tkinter.Tk()
Window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = Window.after(3000, Word_To_English)
# Adding French words to the card
try:
    Fr_data = p.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    Fr_data = p.read_csv("./data/french_words.csv")
Fr_List = Fr_data["French"].to_list()
ToLearn = Fr_data.to_dict(orient="records")
# Making the buttons
Tick_Image = tkinter.PhotoImage(file="./images/right.png")
Check = tkinter.Button(image=Tick_Image, highlightthickness=0, command=Save)
Check.grid(row=1, column=0)
Wrong_Image = tkinter.PhotoImage(file="./images/wrong.png")
Cross = tkinter.Button(image=Wrong_Image, highlightthickness=0, command=UpdateCsv)
Cross.grid(row=1, column=1)
# Setting up the canvas
Canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
Front_Card = tkinter.PhotoImage(file="./images/card_front.png")
Back_Card = tkinter.PhotoImage(file="./images/card_back.png")
FCardImage = Canvas.create_image(400, 263, image=Front_Card)
Word = r.choice(ToLearn)
TitleText = Canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
WordText = Canvas.create_text(400, 263, text="Word", font =("Ariel", 60, "bold"))
Canvas.grid(row=0,column=0, columnspan=2)
Word_Change()
Window.mainloop()





from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"




class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivial")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.quiz_text = self.canvas.create_text(150, 125, width=280, font=("Arial",18,"italic"))
        self.canvas.grid(row=1,column=0, columnspan=2, padx=20, pady=20)

        self.true_img = PhotoImage(file="images\\true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.answer_true)
        self.true_btn.grid(column=0, row=2, padx=20, pady=20)

        self.false_img = PhotoImage(file="images\\false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.answer_false)
        self.false_btn.grid(column=1, row=2, padx=20, pady=20)

        self.score_text = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_text.grid(column=1, row=0)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            quest_text = self.quiz.next_question()
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.quiz_text, text=quest_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text=f"Your final score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def answer_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.feedback(self.quiz.check_answer("False"))
    
    def feedback(self, check):
        if check == True:
            self.canvas.config(bg="green")
        elif check == False:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)


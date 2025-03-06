from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain


        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        #labels
        self.score_label = Label(text="Score: 0",font=("Arial",13),fg="white",bg=THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)

        #canvas
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            text="Q TEXT",
            fill = THEME_COLOR,
            font = ("Arial",20,"italic")
            )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        #buttons
        tick_image = PhotoImage(file=r"C:\Users\RAKESH KUMAR DABAS\PycharmProjects"
                                     r"\PythonProject\day-34\.venv\quizzler-app-start\images\true.png")
        self.true_button = Button(image=tick_image,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        cross_image = PhotoImage(file=r"C:\Users\RAKESH KUMAR DABAS\PycharmProjects"
                                     r"\PythonProject\day-34\.venv\quizzler-app-start\images\false.png")
        self.false_button = Button(image=cross_image,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="Quiz end reached.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



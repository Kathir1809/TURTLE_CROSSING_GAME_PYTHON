FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard:
    def __init__(self):
        self.score = 1
        self.score_b()

    def score_b(self):
        self.tr = Turtle()
        self.tr.color("black")
        self.tr.penup()
        self.tr.hideturtle()
        self.scor()


    def scor(self):
        self.tr.goto(-280,260)
        self.tr.write(f"Level: {self.score}",align="left",font=("Arial Black",13,"normal"))


    def game_over(self):
        self.tr.clear()
        self.tr.goto(0,30)
        self.tr.write(f"Game Over",align="Center",font=("Arial Black",13,"normal"))
        self.tr.goto(0,0)
        self.tr.write(f"You've finished {self.score} level",align="Center",font=("Arial Black",13,"normal"))

    def score_update(self):
        self.score += 1
        self.tr.clear()
        self.scor()
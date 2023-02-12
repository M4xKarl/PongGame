from turtle import Turtle

FONT = ("Courier New", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(275, 210)
        self.write(f"P1: {self.right_score}", align="center", font=FONT)
        self.goto(-275, 210)
        self.write(f"P2: {self.left_score}", align="center", font=FONT)

    def left_scores(self):
        self.left_score += 1
        self.clear()
        self.goto(-275, 210)
        self.write(f"P2: {self.left_score}", align="center", font=FONT)
        self.goto(275, 210)
        self.write(f"P1: {self.right_score}", align="center", font=FONT)

    def right_scores(self):
        self.right_score += 1
        self.clear()
        self.goto(-275, 210)
        self.write(f"P2: {self.left_score}", align="center", font=FONT)
        self.goto(275, 210)
        self.write(f"P1: {self.right_score}", align="center", font=FONT)


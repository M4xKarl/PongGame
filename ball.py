from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
        self.x_move = 1
        self.y_move = 1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

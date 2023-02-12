from turtle import Screen
from scoreboard import Scoreboard
from bat import Bat
from ball import Ball
import time

screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

scoreboard = Scoreboard()
left_bat = Bat((-320, 0))
right_bat = Bat((320, 0))
ball = Ball((0, 0))

screen.listen()
screen.onkey(right_bat.go_up, "Up")
screen.onkey(right_bat.go_down, "Down")
screen.onkey(left_bat.go_up, "w")
screen.onkey(left_bat.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.008)
    screen.update()
    ball.move_ball()

    #Wall Ball Collision
    if ball.ycor() > 240 or ball.ycor() < -232:
        ball.bounce_y()

    #Bat Ball Collision
    if ball.distance(right_bat) < 50 and ball.xcor() > 300 or ball.distance(left_bat) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_scores()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_scores()

screen.exitonclick()

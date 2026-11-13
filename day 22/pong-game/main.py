from turtle import Screen, Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_POSITION = (375, 0)
LEFT_POSITION = (-375, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(RIGHT_POSITION)
left_paddle = Paddle(LEFT_POSITION)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        # Need to bounce
        ball.bounce_y()

    # Detect collision with thepaddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) < 30 and ball.xcor() > -340):
        ball.bounce_x()

    # Detect when right paddle misses the ball
    if ball.xcor() > 375:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -375:
        ball.reset_position()
        scoreboard.right_point()

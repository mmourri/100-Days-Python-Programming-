from turtle import Turtle, Screen
import random

is_race_on = False
colors = [
    "red",
    "blue",
    "green",
    "orange",
    "purple",
    "yellow",
    "pink",
    "cyan",
    "brown"  
]

turtles = []

screen = Screen()
screen.setup(width=500, height=400)
# screen.colormode(255)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_positions = [-120, -90, -60, -30, 0, 30, 60, 90, 120]

for t in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t])
    new_turtle.goto(x=-240, y=y_positions[t])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        random_move = random.randint(0, 10)
        turtle.forward(random_move)


screen.exitonclick()

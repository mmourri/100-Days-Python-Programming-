import turtle as t
from turtle import Turtle, Screen
import random
#  Aliace name for module
# import turtle as t

# tim = t.Turtle()

#  https://cs111.wellesley.edu/reference/colors
#  https://docs.python.org/3/library/turtle.html
#  https://www.w3schools.com/colors/colors_rgb.asp

leo = Turtle()
leo.shape("turtle")
t.colormode(255)
# leo.color("paleGreen4")

print("==================")

# Draw a square
# for _ in range(4):
#     leo.forward(100)
#     leo.right(90)

print("==================")

# Line of dashes
# for _ in range(20):
#     leo.forward(10)
#     leo.penup()
#     leo.forward(10)
#     leo.pendown()

print("==================")

#  Draw shapes

# colors = [
#     "red",
#     "blue",
#     "green",
#     "orange",
#     "purple",
#     "yellow",
#     "cyan",
#     "magenta",
#     "DeepPink",
#     "DarkOliveGreen",
#     "Coral",
#     "Turquoise",
#     "Gold",
#     "RoyalBlue",
#     "Tomato",
#     "Violet",
#     "Salmon",
#     "SkyBlue",
#     "LimeGreen",
#     "Chocolate"
# ]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g, b)
    return color

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         leo.forward(100)
#         leo.right(angle)

# for i in range(3, 11):
#     leo.color(random.choice(colors))
#     draw_shape(i)

print("==================")

#  Random walk
# directions = [0, 90, 180, 270]

# leo.pensize(10)

# for _ in range(200):
#     # leo.color(random.choice(colors))
#     leo.color(random_color())
#     leo.setheading(random.choice(directions))
#     leo.forward(30)

# leo.speed("fastest")

print("==================")

#  Draw spirograph

leo.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        leo.color(random_color())
        leo.circle(100)
        # leo.right(5)
        # leo.left(5)
        leo.setheading(leo.heading() + size_of_gap)

draw_spirograph(5)

print("==================")

screen = Screen()
screen.exitonclick()

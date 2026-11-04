import colorgram
from turtle import Turtle, Screen
import random

# Extract 20 colors from an image
# colors = colorgram.extract('day 18/hirst-painting/hirst-1.jpg', 40)

# Print RGB values
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

colors = [(241, 236, 240), (198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), 
          (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), 
          (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), 
          (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), 
          (67, 86, 23), (219, 206, 8), (181, 186, 213), (46, 72, 57), (168, 201, 212), (100,137, 144)]

leo = Turtle()
screen = Screen()
num_of_dots = 241

leo.penup()
leo.hideturtle()
leo.speed("fastest")
screen.colormode(255)
leo.setheading(225)
leo.forward(500)
leo.setheading(0)

for dot_count in range(1, num_of_dots):
    leo.dot(20, random.choice(colors))
    leo.forward(50)

    if dot_count % 16 == 0:
        leo.setheading(90)
        leo.forward(50)
        leo.setheading(180)
        leo.forward(800)
        leo.setheading(0)
        
screen.exitonclick()

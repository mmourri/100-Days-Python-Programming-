from turtle import Turtle, Screen

#  https://docs.python.org/3/library/turtle.html#turtle.listen
#  https://docs.python.org/3.1/library/turtle.html#turtle.textinput


# def add(n1, n2):
#     return n1 + n2

# def substract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# Higher Order Functions => function that can work with oder function
# def calculator(n1, n2, func):
#     return func(n1, n2)

# result = calculator(2, 3, add)
# print(result)

leo = Turtle()
screen = Screen()

def move_forwards():
    leo.forward(10)

screen.listen()
# function_a(function_b) we pass function in function without ()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()

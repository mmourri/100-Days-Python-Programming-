from turtle import Turtle, Screen
import another_module
from prettytable import PrettyTable

print(another_module.another_variable)

# leo = turtle.Turtle()
leo = Turtle()
print(leo)

leo.shape("turtle")
leo.color("DarkOliveGreen4")

for _ in range(4):
    leo.forward(100)
    leo.left(90)


my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# table.field_names = ["Pokemon Name", "Type"]
# table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Charmander", "Fire"],
#     ]
# )

table.align = "l"

print(table)

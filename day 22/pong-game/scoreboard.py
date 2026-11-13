from turtle import Turtle

ALINGN = "center"
FONT = ("Courier", 60, "normal")
RIGHT_POSITION = (100, 200)
LEFT_POSITION = (-100, 200)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_screboard()
        

    def update_screboard(self):
        self.clear()
        self.goto(LEFT_POSITION)
        self.write(self.left_score, align=ALINGN, font=FONT)
        self.goto(RIGHT_POSITION)
        self.write(self.right_score, align=ALINGN, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update_screboard()

    def right_point(self):
        self.right_score += 1
        self.update_screboard()

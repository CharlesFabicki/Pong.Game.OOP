from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-475, 350)
        self.write(self.l_score, align="center", font=("Arial", 25, "normal"))
        self.goto(475, 350)
        self.write(self.r_score, align="center", font=("Arial", 25, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scores()

    def r_point(self):
        self.r_score += 1
        self.update_scores()

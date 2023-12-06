from turtle import Turtle, Screen
class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.update_scoreboard(self)




        def update_scoreboard(self):
            self.score += 1
            self.textinput(title=f"{self.score}/50 States correct")
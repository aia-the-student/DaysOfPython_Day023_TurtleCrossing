from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORER_POS = (-250, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.penup()
        self.hideturtle()
        self.restart()

    def update_scoreboard(self):
        self.clear()
        self.write('Level: ' + str(self.counter), align='center', font=FONT)

    def add_score(self):
        self.counter += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos((0, 0))
        self.write('Game over.', align='center', font=FONT)

    def restart(self):
        self.clear()
        self.counter = 0
        self.setpos(SCORER_POS)
        self.update_scoreboard()

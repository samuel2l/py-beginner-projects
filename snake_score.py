from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,280)
        #all 3 funcs abv need to occ before you write
        self.write(f"Score: {self.score} ",align="center",font=("Arial",8,"normal"))
        self.hideturtle()


    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 8, "normal"))

    def game_over(self):
        self.goto(0,0)#say game over at screen's center
        self.write("GAMEOVER", align="center", font=("Arial", 8, "normal"))
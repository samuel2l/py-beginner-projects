from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")#food should be circle
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        #shape size initially 20 x 20px
        #applying func abv means you're halving it
        self.color("blue")
        self.speed("fastest")# so relocation of food is swift
        self.refresh()
    def refresh(self):
        #so food goes to rand pos upon collision
        random_pos_x = random.randint(-290, 290)
        random_pos_y = random.randint(-290, 290)
        self.goto(random_pos_x, random_pos_y)

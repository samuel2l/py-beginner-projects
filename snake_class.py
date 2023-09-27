from turtle import Turtle
#self.segments[0] reps the head of the snake
CORs=[(0,0),(0,-20),(0,-40)]
MOVE_DIST=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in CORs:
            self.add_segment(i)
    def add_segment(self,i):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(i)
        self.segments.append(snake_body)

    def grow_snake(self):
        #we go the last element of the list and use the position mtd from the tutrtle class
        self.add_segment(self.segments[-1].position())
        #line abv returns a 2d vector so we extract the coordinates
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        # now we are traversing backwards
        # set the first element to move forward now to achieve the functionality fullyL
        self.segments[0].forward(MOVE_DIST)
    # in order to actually link the various snake segments
    # we need to do it such that the last ele noves to pos of second and second to
    # that of first else the snake parts wont be linked
    # this was the while loop initially:
    #     while game_on:
    #         screen.update()
    #         # move all the parts of the snake in a loop
    #         for i in segments:
    #             i.forward(20)

    # but now in order to achieve the said functionality we loop
    # in the reverse order

#right=0 deg,up= 90 deg,left=180,down=270
    def up(self):
        #if ensures snake cannot go up on itself like in the real game norr
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)


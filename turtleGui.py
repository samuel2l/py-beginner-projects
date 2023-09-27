from turtle import *
from random import *
from prettytable import *


# right(90) means 90 deg to clockwise
# line abv just changes the shape in the middle of screen
# has another class called screen which shows screen turtle will
# show up on
# screen has attributes canvheight, canvwidth
# screen has attributes exitOnClick, canvwidth
# a mtd in the Screen class called bgcolor is used to change the background color of the  canvas
def draw_square():
    my_turtle = Turtle()
    my_turtle.shape("arrow")
    my_turtle.color("blue")
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)


def dashed_line():
    my_turtle2 = Turtle()
    for i in range(15):
        my_turtle2.forward(10)
        my_turtle2.penup()
        # line abv means turtle should not paint on canvas hence the name penup
        my_turtle2.forward(10)
        my_turtle2.pendown()


colors_for_drawing_shape = ["wheat", "SlateGray", "SeaGreen", "IndianRed", "DarkOrchid"]


def draw_shapes(sides):
    my_turtle3 = Turtle()
    my_turtle3.color(choice(colors_for_drawing_shape))
    angle = 360 / sides
    for i in range(sides):
        my_turtle3.forward(100)
        my_turtle3.right(angle)


# for i in range(3,11):
#     draw_shapes(i)


def random_walk():
    my_turtle4 = Turtle()
    directions = [0, 90, 180, 270]  # poss directions the turtle can take in the random walk
    # we can set directions using the normal right and left too
    # but her we will use the setheading that takes an angle as argument

    for i in range(20):
        my_turtle4.color(choice(colors_for_drawing_shape))
        my_turtle4.pensize(10)  # width of pen
        my_turtle4.speed("fastest")  # also takes specified integers eg 1,3,6,10
        my_turtle4.forward(50)
        my_turtle4.setheading(choice(directions))


# random_walk()
# dashed_line()
# draw_square()

# table= PrettyTable()
# #adding to a table using add_column takes a column name and a list of strings entering that column
# table.add_column("First column",["dummy","dummy","dummy","dummy","dummy",])
# table.add_column("Second column",["dummy","dummy","dummy","dummy","dummy",])
# #line below is to align
# table.align="l"
# print(table)
tim = Turtle()
colormode(255)
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.speed("fastest")
draw_spirograph(5)



my_screen = Screen()


my_screen.exitonclick()

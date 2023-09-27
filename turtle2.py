from turtle import Turtle, Screen

tim=Turtle()
screen= Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space",fun=move_forward)
#syntax for calling func is diff cos since we are listening,
#we want to listen before func is used, using the parentheses will give error
#and will also cause func to be exectued regardless

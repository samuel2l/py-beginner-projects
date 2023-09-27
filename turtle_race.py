from turtle import Turtle,Screen
from random import choice,randint
#coordinate in turtle for the heading function:
# east=0, north/up=90,west=180/left,south/down=270
colors = ["wheat", "SlateGray", "SeaGreen", "IndianRed", "DarkOrchid","deep pink","indigo"]

is_race_on=False
screen= Screen()
screen.setup(width=500,height=400)#give screen a size of choice
# so now using the goto function to send the turtle to a specific location
# 0,0 is at center like a normal graph and its max and min val is -height or - width and max +height or + width you barb
user_bet= screen.textinput(title="Make your bet", prompt="which turtle will win the race?Enter a color ")
print(user_bet)

#instead of doing tim.shape("turtle") we can also just initialize the Turtle connstructor
#like so:

#CODE BELOW IS YOUR WORK YOU GOT IT RIGHT BUT WE WILL DO WITH FOR LOOPS

# tim = Turtle(shape="turtle")
# tim.color("red")
# tim.penup()
# timmy = Turtle(shape="turtle")
# timmy.color("blue")
# timmy.penup()
# tom = Turtle(shape="turtle")
# tom.color("DarkOrchid")
# tom.penup()
# tommy = Turtle(shape="turtle")
# tommy.color("cyan")
# tommy.penup()
# tin = Turtle(shape="turtle")
# tin.color("indigo")
# tin.penup()
# tinny = Turtle(shape="turtle")
# tinny.color("deep pink")
# tinny.penup()
# tintin = Turtle(shape="turtle")
# tintin.color("dark goldenrod")
# tintin.penup()
# #the goto func alone will draw a line hence we use a penup
#
# tintin.goto(x=-230,y=190)
# timmy.goto(x=-230,y=140)
# tom.goto(x=-230,y=80)
# tommy.goto(x=-230,y=20)
# tinny.goto(x=-230,y=-40)
# tim.goto(x=-230,y=-100)
# tin.goto(x=-230,y=-160)
y_pos=[-160,-100,-40,20,80,140 ,190]
all_turtles=[]
for turtle_index in range(7):
    tim= Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_pos[turtle_index])
    all_turtles.append(tim)
if user_bet:
    is_race_on= True
winning_color=""
while is_race_on:
    #in order to end the race we check x coordinate

    for turtle in all_turtles:

        if turtle.xcor()>230:
            is_race_on=False
            winning_color= turtle.pencolor()
            if winning_color==user_bet:
                print("Your turtle won wowwwwww")
            else:
                print("Your turtle lost chale")
        dist = randint(0, 10)
        turtle.forward(dist)
    print(f"the winnner is the {winning_color} turtle")



screen.exitonclick()
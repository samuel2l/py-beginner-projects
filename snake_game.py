from turtle import Screen, Turtle
from time import *

from snake_class import Snake
from snake_food import Food
from snake_score import Score

screen= Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
#line abv turns off the trace
#In the turtle module, the screen.tracer() method is used to control
# the animation speed of the turtle graphics. The tracer() method allows you to specify how
# many turtle actions (such as movements, drawings, etc.) should be buffered before updating the screen.
# This can make the animation smoother and faster
# the screen.tracer(0) line disables automatic animation.
# The loop draws a complex shape using the turtle, and the screen is manually updated using screen.update() after the shape is complete.
# This way, you can control when the screen updates and show the final result without displaying the intermediate steps of the animation.




snake = Snake()
food= Food()
score= Score()
screen.listen()
#notice here too you dont add the () to the function
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
#so after you have finished updating the snake body now display the animation using scren.update

# or you can use tuples
#starting_pos=[(0,0),(-20,0),(-40,0)]
# for i in range(starting_pos):
#     snake_body= Turtle(shape="square")
#     snake_body.color("white")
#     snake_body.goto(i)

# okay now code below will animate the snake:
game_on=True
#good practice to use flags
while game_on:
    screen.update()
  #if statement to increase speed as your score gets higher
    if score.score < 10:
        sleep(0.3)
    else:
        sleep(0.1)



    #move all the parts of the snake in a loop
    snake.move()
    #detect collision with food. done using the distance mtd
    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.grow_snake()
        score.increase_score()
    #to check when snake hits bound game is over
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280:
        game_on = False
        score.game_over()
    #if snake hits itself game over:
    for i in snake.segments[1:]:#slice so it skips the first iter where i is the head since atp it will just say game over you barb
        if snake.segments[0].distance(i)<10: #and i!=snake.segments[0]:
            game_on=False
            score.game_over()
screen.exitonclick()

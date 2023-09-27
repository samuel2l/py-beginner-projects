#upon exiting the canvas is still there, get why
import turtle

import pandas as pd
screen= turtle.Screen()
screen.title("States Game")
#line below to add the gif image
#add shape property is used to achieve this and it takes a path as param
screen.addshape('../states game/blank_states_img.gif')

turtle.shape('../states game/blank_states_img.gif')

# def get_mouse_click_cor(x,y):
#     print(x,y)
#func abv will print coordinates of all clicks to screen
#onscreenclick(get_mouse_click_cor)
score=0
#while True:
#print(user_ans)
data=pd.read_csv('../states game/50_states.csv')

all_states=data.state.to_list()
#explicitly giving it a tuple wont work I think it has to do with the fact that its a series and we cannot change series type
#so we need to give two cors in the goto method as ints, dont really get why that will work mmom
#cors = (int(x_cor), int(y_cor))
#if statement below was me using the check and seeing if it was true
# wont work as expected since series dont have bool values you barb
already_answered=[]
while True:
    user_ans = screen.textinput(title=f"{score}/50 correct", prompt="Guess a state").title()
    if user_ans in all_states and user_ans not in already_answered:
        ans_on_screen= turtle.Turtle()
        ans_on_screen.hideturtle()
        ans_on_screen.penup()
        ans_on_screen.goto(int(data[data.state==user_ans].x),int(data[data.state==user_ans].y))
        ans_on_screen.write(user_ans)
        score+=1
        already_answered.append(user_ans)
        if score==50:
            print("Congratssssss")
    elif user_ans == 'Exit':
        break


      #
        #
        #
        #
        # if user_ans in data["state"]:
        #
        #     score+=1
        #     print(score)
        #     if score==50:
        #         print("congratss")
    unable_to_guess = []
    for i in all_states:

            if i in already_answered:
                continue
            else:
                unable_to_guess.append(i)

    #print(unable_to_guess)
    data_dict = {
       # "Correct guesses": already_answered,
        "Unable": unable_to_guess
        }
    df= pd.DataFrame(data_dict)
    df.to_csv('results.csv')



    #to ensure screen is always on use mainloop
#now we will let you know the states you guessed right and ones you couldnt using csv files


screen.mainloop()

#screen.exitonclick()
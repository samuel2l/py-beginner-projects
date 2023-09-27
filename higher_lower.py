from higher_lower_data import *
from random import *
from replit import *
# for i in data:
#     print(i["name"])

#print(data[0]["name"])
print(logo)
score = 0
score= int(score)
while True:

    rand = choice(data)
    print("Compare A: ",rand["name"],": a ",rand["description"],"from ",rand["country"])

    rand2 = choice(data)
    print(vs)
    print("against B: ",rand2["name"],": a ",rand2["description"],"from ",rand2["country"])
    answer=input('Who has more followers? A or B ').upper()

    if answer == 'A':
        if rand["follower_count"] > rand2["follower_count"]:
            print("You are right")

            score += 1
            print(score)
        else:
            print("Not true")
            print("Your final score is ", score)
            break
    elif answer=='B':
        if rand2["follower_count"] > rand["follower_count"]:
            print("You are right")
            score += 1
            print(score)
        else:
            print("Not true")
            print("Your final score is ", score)
            break
    else:
        print("Invalid input")

import requests
import datetime as dt

APP_ID = "3f488282"
API_KEY = "013769bf7a47116ba4877f1b8a11ce74"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    #"x-remote-user-id": "0"


}
post_param={
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint,json=post_param,headers=headers)
exercise_data = response.json()
print(exercise_data)
#so now we take the data from the exercise api and use it to add a row in the google sheet using the sheety API
sheet_post_endpoint = "https://api.sheety.co/70248c8c38f210c1c7e41fb0cefa6d46/workoutTracker/workouts"
#the keys in the sheet_post_params are the columns in the datasheet as we are adding rows that must correspond to the columns
#
today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")
print(today_date,now_time)
print(dt.datetime.now().strftime('%d/%m/%Y'),dt.datetime.now().strftime('%X'))
#GET WHY THIS DOES NOT WORK FOR A SPECIFIC INDEX IN LIST
# sheet_post_params={
#   "workouts": {
#       "date": dt.datetime.now().strftime('%d/%m/%Y'),
#       "time": dt.datetime.now().strftime('%X'),
#       "exercise": exercise_data["exercises"][0]["name"].title(),
#       "duration": exercise_data["exercises"][0]["duration_min"],
#       "calories": exercise_data["exercises"][0]["nf_calories"]
#
#   }
# }
#need to loop as data is a list so a separate request is sent for every exercise
for exercise in exercise_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_post_request = requests.post(url=sheet_post_endpoint,json=sheet_inputs,auth=('sam22ul','efe'))
    print(sheet_post_request.text)

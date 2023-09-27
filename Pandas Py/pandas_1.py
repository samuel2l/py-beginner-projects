import csv
import pandas as pd
#data=pd.read_csv('weather_data.csv')
#print(data["temp"].mean())

#print(data["temp"])
#line below will not work cos to_list is a prop of a series
#data_list= data.to_list()
#print(data["temp"].max())
#print(data[data.day=='Monday'])
#get row with maximum temp:
# max_temp=data[data.temp==data.temp.max()]
# print(max_temp.condition)
data = pd.read_csv('../2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels=len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrels)

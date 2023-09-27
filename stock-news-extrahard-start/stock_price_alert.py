import time
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
import requests
import datetime as dt
api_key="CTJEP6UFVR3WTDSM"
params={
    'function':'TIME_SERIES_DAILY',
    'symbol': 'IBM'
}
response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}',params=params)
data = response.json()
# print(data['Meta Data'])
#print(data['Time Series (Daily)'])
dates=[]
for key,value in data.items():
    if key=='Time Series (Daily)':
        for key,value in data[key].items():

            dates.append(key)
        print(f' old {len(dates)}')

        open=data['Time Series (Daily)'][dates[0]]["1. open"]
        close=data['Time Series (Daily)'][dates[1]]["4. close"]
        #difference=open-close
        dates.remove(0['Time Series (Daily)'][dates[0]])
        dates.remove(data['Time Series (Daily)'][dates[1]])
        print(f'new length {len(dates)}')
        time.sleep(86400)



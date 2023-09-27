import requests
import datetime as dt
import spotipy
import spotipy.oauth2

from bs4 import BeautifulSoup
CLIENT_ID="aa1668efeaaf490caf4dc2418a5b6aae"
client_secret="0d3e9a775f1b490a8b4fabe06d65b267"
year= input("what time would you like to go back to?")

response= requests.get(f"https://www.billboard.com/charts/hot-100/{year}/#")
web_data=response.text
soup=BeautifulSoup(web_data,"html.parser")
song_html=soup.select("li ul li h3")
song_list=[]
for i in song_html:
    #we need to strip cos data comes with plenty unnecessary empty spaces
    song_list.append(i.getText().strip())

print(song_list)
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
#
# requests.get(url, auth=auth)

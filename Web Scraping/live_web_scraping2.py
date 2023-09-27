from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_data = response.text
soup = BeautifulSoup(web_data, "html.parser")
#print(soup.title)
titles = soup.find_all(name="li")
print(titles)

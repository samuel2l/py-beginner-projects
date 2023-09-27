from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
web_data = response.text
soup = BeautifulSoup(web_data, "html.parser")
titles = soup.find_all(class_="titleline")
print(titles)
headings=[]
links=[]


for title in titles:
    text=title.getText()

    headings.append(text)



vote_int=[]
vote_list=[]
article_upvote = soup.find_all(class_="score")
for vote in article_upvote:

    vote_int.append(int(vote.getText()[:-7]))
# print(vote_list)
# print(links)
print(headings)
k=sorted((vote_list))
print(k[-1])
for i in range(len(vote_list)):
    if vote_list[i]==k[-1]:
        print(links[i])
        print(vote_int[i])
        print(headings[i])

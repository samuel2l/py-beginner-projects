from bs4 import BeautifulSoup
#some websites give error when using html.parser
#if so then use lxml
#import lxml

with open('website.html', encoding='utf-8') as file:
    contents = file.read()
soup=BeautifulSoup(contents,"html.parser")
#print(soup)#gives you all the data in the html
#print(soup.prettify())#gives you all the data in a prettier way

# #o/p with content and tags
#print(soup.title)

#o/p has only content
#print(soup.title.string)
# note that the soup.tag notation only returns the first of its type
# it does not actually parse through the html to find every occ of the specified tag
#to get all:
#find all gives a list of elements of the type specified
all_tags=soup.find_all(name="a")
#to be able to print the text since issa list obv we will need a loop
for tag in all_tags:
    print(tag.getText())

# to get a specific attribute of tag eg like href,class etc:
    print(tag.get("href"))
# to find a specific element:
search=soup.find_all(class_= "heading")
print(search)

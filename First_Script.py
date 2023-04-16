import requests
from bs4 import BeautifulSoup

page = requests.get("https://russellinvestments.com/uk/about-us")   #This statement will assign the targeted web page's URL.
souped = BeautifulSoup(page.content, "html.parser") #Assigning the whole page source code content to the 'souped' variable.
#print(souped) #Print the souped variable value.

imgs = souped.find_all("img") #Use this to find all img tags in the page source code.

print(imgs)
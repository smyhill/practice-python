# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features='lxml')
titles = ""
for title in soup.find_all('h3', 'e1lsht870'):
    titles += str(title.text)
    titles += str(", ")

print(titles)

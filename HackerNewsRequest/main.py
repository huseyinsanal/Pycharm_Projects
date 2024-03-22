import requests
from bs4 import BeautifulSoup


target_url = "https://news.ycombinator.com/"

response = requests.get(target_url)

soup = BeautifulSoup(response.text)

print(soup.get_text())


#html parsing
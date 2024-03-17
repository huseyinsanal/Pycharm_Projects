import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the URL of the webpage you want to access
response = requests.get("https://news.ycombinator.com/")
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
# Extract the text content of the webpage
text = soup.get_text()

print(text)

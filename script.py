import requests
from bs4 import BeautifulSoup

url = 'http://everynoise.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
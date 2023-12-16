import requests
from bs4 import BeautifulSoup

url = 'https://tengrinews.kz/news/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

zagolovki = soup.find_all('span', class_='tn-article-title')

for zagolovok in zagolovki:
    print(zagolovok.text)
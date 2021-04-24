from bs4 import BeautifulSoup
import requests, webbrowser

search_string = 'nat geo wild'
search_string = search_string.replace(' ', '+')
print(search_string)
search_url = f'https://google.com/search?q={search_string}'
print(search_url)
#webbrowser.open(search_url)
response = requests.get(search_url)
print(response, response.ok)
response = response.text
soup = BeautifulSoup(response, 'lxml')
print(soup.prettify())

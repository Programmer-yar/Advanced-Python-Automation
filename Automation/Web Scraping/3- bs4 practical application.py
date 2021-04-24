from bs4 import BeautifulSoup
import requests

#stores 'html' of full page
source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')
# article = soup.find('article')
# print(article.prettify(), '\n'*2)
# print(article.header.h2.a.text, '\n'*2)
# print(article.div.p.text)

for article in soup.find_all('article'):
    print('Heading: \n', article.header.h2.a.text, '\n')
    print('Summary: \n', article.div.p.text)
    print('*'*40, '\n')

print(len(soup.find_all('article')), '\n')
link = soup.find('iframe', class_="youtube-player")

#attributes of a tag can be accessed like a dictionary
# e.g class, id, src attribute of an html element
vid_source = link['src']
print(vid_source.split('/'), '\n')

vid_id = vid_source.split('/')[4]
vid_id = vid_id.split('?')[0]
print('Video ID: ', vid_id, '\n')

#generating YouTube link using video id
youtube_link = f'https://youtube.com/watch?v={vid_id}'
print(youtube_link)

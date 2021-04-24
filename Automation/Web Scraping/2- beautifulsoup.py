from bs4 import BeautifulSoup

with open('sample_page.html') as html_file:
    #BeautifulSoup(file_name, parser)
    soup = BeautifulSoup(html_file, 'lxml')

#prints full html code of the page
#print(soup, '\n'*2)

#'prettify()' method
#prints formatted html code of the page
print(soup.prettify(), '\n'*2)

#gets html tag by attribute (also includes html tag)
page_title = soup.title
print(page_title, '\n'*2)

#gets only the text within the tag
page_title = soup.title.text
print(page_title, '\n'*2)

#get the first '<div>' on the page
div = soup.div.prettify()
print(div, '\n'*2)

#'find()' method, 
#gets single element matching arguments
my_div = soup.find('div', class_='article')

#gives first div with the class of article
print(my_div, '\n'*2)

#digs into div > h3 > a(anchor tag)
headline = my_div.h3.a.text
print(headline, '\n'*2)

summary = my_div.p.text
print(summary, '\n'*2)

# 'find_all()' method
# makes a list of all elements filtered according to given parameters
for article in soup.find_all('div', class_='article'):
    print(article.h3.a.text, '\n', article.p.text, '\n')














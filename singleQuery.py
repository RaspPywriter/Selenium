import requests
from bs4 import BeautifulSoup 
f = open('cities.txt', 'r')
s = open('searches.txt', 'r')
newFile = open('soupOutput.txt', 'wb')

for l in f:   
    i = l.strip('\n')
    for t in s:
        query = t.strip('\n')
    url = 'https://'+i+'.craigslist.org/search/aos?query='+query
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib') 
    for listing in soup.find_all('li', {'class':'result-row'}):
        title = listing.find('p').find('a').text
        link = listing.find('a')['href']
        newFile.write((title+'\n').encode('utf-8'))
        newFile.write((link+'\n').encode('utf-8'))

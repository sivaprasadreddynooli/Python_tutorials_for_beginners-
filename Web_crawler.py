#there are number of ways of connecting to the internet , below one being the most preferred
#Beautifulsoup - this helps in crawling through the websites and collect the information of various links
import requests
from bs4 import BeautifulSoup

def trade_spider(max_apges):
    page = 1
    while page<= max_apges:
        url = 'http://buckysroom.org/trade/search.php?page=2' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class':'item-name'}):
            href =  'http://buckysroom.org' + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div',{'class':'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://buckyroom.org" + link.get('href')
        print(href)


trade_spider(3)




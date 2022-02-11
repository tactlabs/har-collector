
'''
Created on 

Course work: 

@author: Chaaya, Aravind

Source: 

    
'''
import requests
from bs4 import BeautifulSoup
import csv
import time

import logging

logging.basicConfig(
    filename = 'datacollector.log', 
    level = logging.DEBUG
)

def read_file():

    # open the data file
    file = open("urls.txt")
    
    # read the file as a list
    data = file.readlines()
    
    # close the file
    file.close()

    new_data = []
    for item in data:
        item = item.replace('\n', '')
        print(f'item : {item}')
        new_data.append(item)

    # print(data)
    return new_data

def test():

    URL = "http://www.values.com/inspirational-quotes"
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'html5lib')
    
    quotes=[]  # a list to store quotes
    
    table = soup.find('div', attrs = {'id':'all_quotes'}) 
    
    for row in table.findAll('div',
                            attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
        quote = {}
        quote['theme'] = row.h5.text
        quote['url'] = row.a['href']
        quote['img'] = row.img['src']
        quote['lines'] = row.img['alt'].split(" #")[0]
        quote['author'] = row.img['alt'].split(" #")[1]
        quotes.append(quote)
    
    filename = 'inspirational_quotes.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['theme','url','img','lines','author'])
        w.writeheader()
        for quote in quotes:
            w.writerow(quote)

def collect_data_single(url):

    source = requests.get(url).text
    soup = BeautifulSoup(source, "lxml")

    # Sleep 10 seconds as a testing to slow down things
    # time.sleep(10)

    title = soup.find('title').string
    logging.info(f'title: {title}')

    if(not title or 'Not Found' in title):
        logging.error('404 Error Found')
    else:
        logging.info(f'url : {url}, title : {title}')

    # article = soup.find("article", class_ = "content post-249781 post type-post status-publish format-standard hentry category-python tag-python-list-programs tag-python-list")
    # article_text = article.find("div", class_ = "text")
    # methods = article_text.find_all("p")
    # for method in methods:
    #     print(method.text)

def collect_multiple(url_list):
    
    for url in url_list:
        # print(f'collecting url : {url}')
        collect_data_single(url)

    print('All URLs collected')


def startpy():

    '''
        'https://www.kijiji.ca/v-cars-trucks/calgary/2020-ford-f150-xlt/m2344600',
        'https://www.kijiji.ca/v-cars-trucks/calgary/2020-ford-f150-xlt/m2344693'
    '''

    # collect_data_single("https://www.kijiji.ca/v-cars-trucks/calgary/2020-ford-f150-xlt/m2344600")

    # url_list = [
    #     'https://www.kijiji.ca/v-cars-trucks/calgary/2020-ford-f150-xlt/m2344600',
    #     'https://www.kijiji.ca/v-cars-trucks/calgary/2020-ford-f150-xlt/m2344693'
    # ]

    # collect_multiple(url_list)

    url_list = read_file()
    print(url_list)
    collect_multiple(url_list)

if __name__ == "__main__":
    startpy() 


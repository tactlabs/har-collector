'''
Created on 

Course work: 

@author: Ana, Chaaya, Sanjju, Ishita

Source: 

    
'''

import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import lxml
# import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import csv
import logging
import random

logging.basicConfig(
    filename    = 'datacollector.log', 
    level       = logging.DEBUG
)

LINK_FILEPATH = "kijiji_cars_links.txt"
DEST_FILEPATH = 'output1.csv'

def getTitle(soup):
    try:
        return soup.find('h1', class_ = "title-2323565163").text
    except:
        return "None"

def getInfo(soup):
    try:
        return soup.find('span', class_ = "currentPrice-2842943473").text
    except:
        return "None"

def getDescription(soup):
    try:
        return soup.find('div', class_ = "descriptionContainer-231909819").text
    except:
        return "None"

def getApplication(soup):
    try:
        return soup.find('span', class_ = "address-3617944557").text
    except:
        return "None"   

def collectpy(urlList):

    with open(DEST_FILEPATH, 'w', newline = '')  as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerow(['Title', 'Info', 'Desc', 'Application'])
        
        for url in urlList:
            print(url)
            try:
                html = urlopen(url)
                logging.info(f'url collected : {url}')
            except HTTPError as http_err:
                print(f'http error : {http_err},')
                logging.error(f'http error : {http_err}')
            except URLError as url_err:
                print(f'url error : {url_err}')
                logging.error(f'url error : {url_err}')
            else:
                soup = BeautifulSoup(html.read(),"html5lib")
                row = [getTitle(soup), getInfo(soup), getDescription(soup)]
                # print(row)
                csv_output.writerow(row)

def get_random_number():

    return random.randint(10, 100)

# Not used as it is not very effective for our business case
def match_item(c_rand_number, index):

    if(c_rand_number % 5 == index):
        print(f'entered_5: {c_rand_number}, {index}')
        return True

    if(c_rand_number % 4 == index):
        print(f'entered_4: {c_rand_number}, {index}')
        return True

    if(c_rand_number % 3 == index):
        print(f'entered_3: {c_rand_number}, {index}')
        return True

    if(c_rand_number % 9 == index):
        print(f'entered_9: {c_rand_number}, {index}')
        return True

    if(c_rand_number % 11 == index):
        print(f'entered_11: {c_rand_number}, {index}')
        return True

    if(c_rand_number % 2 == index):
        print(f'entered_2: {c_rand_number}, {index}')
        return True

    return False

def read_file(inject_random_error = False):

    # open the data file
    file = open(LINK_FILEPATH, "r")
    
    # read the file as a list
    data = file.readlines()
    
    # close the file
    file.close()

    new_data = []
    for index, item in enumerate(data):
        item = item.replace('\n', '')

        if(index % 6 == 0):

            item = str(item) + 'sdi3739djysy'

            print(f'{index} : item : {item}')

        new_data.append(item)

    # print(new_data)
    return new_data

def startpy():

    urlList = read_file()
    collectpy(urlList)

if __name__ == "__main__":
    startpy()  
'''
Created on 

Course work: 

@author: Ana

Source: 

    
'''

import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import lxml
import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import csv


def getTitle(soup):
    return soup.find('h1', class_="title-2323565163").text

def getInfo(soup):
    return soup.find('ul', class_="itemAttributeList-1090551278").text

def getDescription(soup):
    return soup.find('div', class_="descriptionContainer-231909819").text

def getApplication(soup):
    return soup.find('span', class_="address-3617944557").text

urlList =  [
        'https://www.kijiji.ca/v-cars-trucks/calgary/2020-ford-f150-xlt/m2344600',
        'https://www.kijiji.ca/v-cars-trucks/calgary/2020-ford-f150-xlt/m2344693'
    ]

with open('output.csv', 'w', newline='')  as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(['Title', 'Info', 'Desc', 'Application'])
    
    for url in urlList:
        try:
            html = urlopen(url)
        except HTTPError as e:
            print(e)
        except URLError:
            print("error")
        else:
            soup = BeautifulSoup(html.read(),"html5lib")
            row = [getTitle(soup), getInfo(soup), getDescription(soup), getApplication(soup)]
            print(row)
            csv_output.writerow(row)
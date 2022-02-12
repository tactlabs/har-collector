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
import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import csv
import logging

logging.basicConfig(
    filename = 'datacollector.log', 
    level = logging.DEBUG
)


def getTitle(soup):
    try:
        return soup.find('h1', class_="title-2323565163").text
    except:
        return "None"

def getInfo(soup):
    try:
        return soup.find('span', class_="currentPrice-2842943473").text
    except:
        return "None"

def getDescription(soup):
    try:
        return soup.find('div', class_="descriptionContainer-231909819").text
    except:
        return "None"

def getApplication(soup):
    try:
        return soup.find('span', class_="address-3617944557").text
    except:
        return "None"   

def collectpy(urlList):


    with open('output1.csv', 'w', newline='')  as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerow(['Title', 'Info', 'Desc', 'Application'])
        
        for url in urlList:
            print(url)
            try:
                html = urlopen(url)
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

def read_file():

    # open the data file
    file = open("kijiji_cars_links.txt", "r")
    
    # read the file as a list
    data = file.readlines()
    
    # close the file
    file.close()

    new_data = []
    for item in data:
        item = item.replace('\n', '')
        # print(f'item : {item}')
        new_data.append(item)

    # print(new_data)
    return new_data

def startpy():

    urlList = read_file()
#     urlList = ["https://www.kijiji.ca/v-cars-trucks/timmins/2018-chevrolet-silverado/m2731021",
# "https://www.kijiji.ca/v-cars-trucks/brantford/2020-chevrolet-corvette-2dr-stingray-cpe-2lt-glass-roof-front-lift/m2582223",
# "https://www.kijiji.ca/v-cars-trucks/st-catharines/2018-hyundai-santa-fe-xl-xl-premium-all-wheel-drive-7-passenger/m2522768"]

    collectpy(urlList)

if __name__ == "__main__":
    startpy()  
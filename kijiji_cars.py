'''
Created on 

Course work: 

@author: Elakia, Sanjjushri

Source: 

    
'''

import re
import requests
from bs4 import BeautifulSoup


for page_no in range (1, 24):
    r = requests.get("https://www.kijiji.ca/b-cars-trucks/ontario/cars/page-{}/k0c174l9004".format(page_no))
    data = r.content  
    soup = BeautifulSoup(data, "html.parser")


    for i in soup.find_all('div',{'class':'title'}):

        link = i.find('a',href=True, attrs={'href': re.compile("^http://")})
        
        if link is None:
            continue
            
        car_links = ('https://www.kijiji.ca{}\n'.format(link['href']))
        print(car_links) 
    

        file = open("kijiji_cars_links.txt","a")
        file.write(car_links)
        file.close()

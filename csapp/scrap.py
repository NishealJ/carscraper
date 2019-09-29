from django.shortcuts import render

import requests

from bs4 import BeautifulSoup

session = requests.Session()
session.headers = {"",""}

def scrape_car_maker():

    url = "https://www.cardekho.com/filter/new-cars"
    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html5lib")

    car_list_raw = soup.find_all('input', {'name':'brands'})
    car_list = [] 

    for car_list_input_tag in car_list_raw:
       car_list.append(car_list_input_tag.get('value'))

    return car_list

def scrape_car_models(maker):

    url = "https://www.cardekho.com/cars/"+maker
    content = session.get(url, verify=False).content

    car_list_req = []

    soup = BeautifulSoup(content, "html5lib")
    get_cars_by_req = soup.findAll('div', attrs={'class':'gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder'})

    for car_divs in get_cars_by_req:
        car_list_req.append(car_divs.find('a').contents[0])

    return car_list_req


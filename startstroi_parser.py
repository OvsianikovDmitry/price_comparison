import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
import json


# def pars():
"""Спарсить общие категории"""
#     HEADERS ={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
#
#
#     url = 'https://startstroi.by/catalog/'
#     req = requests.get(url, headers=HEADERS)
#     req.encoding='utf-8'
#     resp = req.text
#
#     all_categories = {}
#
#     soup = BeautifulSoup(resp, 'lxml')
#
#     name_category = soup.find_all('div', class_='subcategories__block')
#
#     for i in name_category:
#         name = i.find('div', class_='subcategories__title-info').find('p', class_='subcategories__subcat-title').text.strip()
#         link = 'https://startstroi.by' + i.find('div', class_='subcategories__title-info').find('p', class_='subcategories__subcat-title').find('a').get('href')
#         all_categories[name]= link
#
#     with open ('all_categories_starstroi_new.json', 'w', encoding='utf-8') as file:
#         json.dump(all_categories,file, indent=4, ensure_ascii=False)



# with open ('all_categories_starstroi.json', encoding='utf-8') as file:
#     all_categ = json.load(file)
#
# for k,v in all_categ.items():
#     url=v
#     req = requests.get(url)
#     req.encoding = 'utf-8'
#     res = req.text
#     soup = BeautifulSoup(res,'lxml')
#
#     products = soup.find_all('div',class_='product-card__info-block')
#     for i in products:
#         cards = i.find('a', class_='product-card__see-more btn-prime').get('href')
#         name = cards.find('h1', class_='product__title').text + cards.find('div', class_='product__variation-group')
#         print(name)


    # show_more = soup.find('div',class_='products__row').get('data-url')
    # print(show_more)
    # print(type(show_more))

"""Спарсить все товары по каждой"""
def pars():
    HEADERS ={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}


    url = 'https://startstroi.by/catalog/'
    req = requests.get(url, headers=HEADERS)
    req.encoding='utf-8'
    resp = req.text

    all_categories = {}

    soup = BeautifulSoup(resp, 'lxml')

    name_category = soup.find_all('a', class_='subcategories__producer-link')

    for i in name_category:
        name = i.text.strip()
        link = 'https://startstroi.by' + i.get('href')
        all_categories[name]= link

    with open ('all_categories_starstroi_new.json', 'w', encoding='utf-8') as file:
        json.dump(all_categories,file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    pars()

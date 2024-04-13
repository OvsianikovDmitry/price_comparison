import requests
from bs4 import BeautifulSoup
import json
import csv
from time import sleep

HEADERS = {
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }


JSON_FILE = 'stroyBaza_all_category_links.json'


# url = "https://stroybaza.by/catalog/"
#
# req = requests.get(url, headers=HEADERS)
# req.encoding='utf-8'
# src = req.text
#
# link_category = {}
#
# soup = BeautifulSoup(src, 'lxml')
#
# name_categ = soup.find_all('div', class_='catalog-section-child')
#
# count=0
# for i in name_categ:
#
#     name = i.text.strip()
#     link = 'https://stroybaza.by'+i.find('a').get('href')
#     link_category[name] = link
#
# with open('stroyBaza_all_category_links.json', 'w', encoding='utf-8') as file:
#     json.dump(link_category, file, indent=4, ensure_ascii=False)

with open('stroyBaza_all_category_links.json', encoding='utf-8') as file:
    all_categories = json.load(file)
    print(all_categories)

def get_text(el):
    if not el:
        return ''
    return el.get_text(strip=True)

def get_html(j_file):
    with open(j_file, encoding='utf-8') as file:
        category = json.load(file)
    count=0
    if count<2:
        for k,v in category.items():

            url = v
            req = requests.get(url,headers=HEADERS)
            req.encoding='utf-8'
            res =req.text
            soup = BeautifulSoup(res, 'lxml')

            items = soup.find_all('div', class_='catalog-item-info catalog-item-linkarea')

            cards = []
            print('GET CONTENT')
            for i in items:
                cards.append({
                    'title': i.find('div', class_='item-all-title').get_text(strip=True),
                    'price': get_text(i.find('span', class_='catalog-item-price'))
                })
            with open(f'{k}.csv', 'w', newline='',encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['Наименование', 'Стоимость'])
                for card in cards:
                    writer.writerow([card['title'], card['price']])
                    print('SAVE')
            sleep(2)
            count+=1
        return print('GameOver')


get_html(JSON_FILE)
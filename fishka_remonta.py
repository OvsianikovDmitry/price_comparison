import requests
from bs4 import BeautifulSoup
import csv
import json
from time import sleep


HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
JSON_FILE = 'data_fishka_remonta/fishka_remonta_all_category_links.json'

# url ="https://fishkaremonta.by/catalog/"
# req = requests.get(url, headers=HEADERS)
# req.encoding='utf-8'
# scr = req.text
#
# soup = BeautifulSoup(scr, 'lxml')
#
# categ = soup.find_all('a')
#
#
# w_link={}
# for i in categ:
#     link = i.get('href')
#     name = i.text.strip()
#     print(link)
#     categ_link = f'https://fishkaremonta.by{link}'
#     w_link[name]=categ_link
#
# with open ('data_fishka_remonta/fishka_remonta_all_category_links_new.json', 'w', encoding='utf-8') as file:
#     json.dump(w_link, file, indent=4, ensure_ascii=False)


def get_text(el):
    if not el:
        return ''
    return el.get_text(strip=True)


"""ПАРСЕР С ПАГИНАЦИЕЙ"""

def get_html(j_file):
    with open(j_file, encoding='utf-8') as file:
        category = json.load(file)

    for k,v in category.items():
        next_page=''
        cards = []
        while next_page != 'stop':
            print('step')
            print(next_page)
            url = f'{v}{next_page}'
            print(url)
            req = requests.get(url,headers=HEADERS)
            req.encoding='utf-8'
            res =req.text
            soup = BeautifulSoup(res, 'lxml')

            items = soup.find_all('div', class_='product-item')

            print('GET CONTENT')
            for i in items:
                cards.append({
                    'title': i.find('div', class_='poduct-item-title').get_text(strip=True),
                    'price': get_text(i.find('span', class_='product-item-price-current'))
                })

            show_more = soup.find('div', class_='catalog-section-more')
            if not not show_more :
                try:
                    page = soup.find('div', class_='catalog-section-pagination').find('li', class_='last').find('a').get('href')
                    print(page)
                    next_page = page.split('/')[-1]

                except:
                    continue
            else:
                next_page='stop'

        with open(f'data_fishka_remonta/{k}.csv', 'w', newline='',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Наименование', 'Стоимость'])
            for card in cards:
                writer.writerow([card['title'], card['price']])
                print('SAVE')
        sleep(2)

    return print('GameOver')


get_html(JSON_FILE)
import requests
from bs4 import BeautifulSoup
import json
import csv
from time import sleep

HEADERS = {
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }


JSON_FILE = 'data_mamont/mamont_all_category_links.json'
# JSON_FILE = 'data_mamont/test_json'


#
# url = "https://mamont.by/catalog/"
#
# req = requests.get(url, headers=HEADERS)
# req.encoding='utf-8'
# src = req.text
#
# link_category = {}
#
# soup = BeautifulSoup(src, 'lxml')
#
# name_categ = soup.find_all('div', class_='section')
#
# count=0
# for i in name_categ:
#
#     name = i.text.strip()
#     link = 'https://mamont.by'+i.find('a').get('href')
#     link_category[name] = link
#
# with open('data_mamont/mamont_all_category_links.json', 'w', encoding='utf-8') as file:
#     json.dump(link_category, file, indent=4, ensure_ascii=False)

# with open('data_mamont/mamont_all_category_links.json', encoding='utf-8') as file:
#     all_categories = json.load(file)
#     print(all_categories)

def get_text(el):
    if not el:
        return ''
    return el.get_text(strip=True)

def get_html(j_file):
    with open(j_file, encoding='utf-8') as file:
        category = json.load(file)

    for k,v in category.items():
        cards = []
        url = v
        req = requests.get(url,headers=HEADERS)
        req.encoding='utf-8'
        res =req.text
        soup = BeautifulSoup(res, 'lxml')
        try:
            pages_count = soup.find('div', class_='bx-pagination-container row').find_all('a')
            print(len(pages_count))
            all_tovar_in_pages = 0
            for page in range(1, len(pages_count) + 1):
                url = f'{v}?PAGEN_4={page}'
                response = requests.get(url=url, headers=HEADERS)
                response.encoding = 'utf-8'
                res = response.text
                soup_1 = BeautifulSoup(res, 'lxml')
                items = soup_1.find_all('div', class_='tabloid nowp')
                x = len(items)
                all_tovar_in_pages += x

                # print('GET CONTENT')

                for i in items:
                    cards.append({
                        'title': i.find('span', class_='middle').get_text(strip=True),
                        'price': get_text(i.find('span', class_='price getPricesWindow'))
                    })


        except Exception:
            print('No pagination')
            url = v
            response = requests.get(url=url, headers=HEADERS)
            response.encoding = 'utf-8'
            res = response.text
            soup_1 = BeautifulSoup(res, 'lxml')
            items = soup_1.find_all('div', class_='tabloid nowp')
            all_tovar_in_pages = len(items)

            # print('GET CONTENT')
            for i in items:
                cards.append({
                    'title': i.find('span', class_='middle').get_text(strip=True),
                    'price': get_text(i.find('span', class_='price getPricesWindow'))
                })


        count = 1
        with open(f'data_mamont/{k}.csv', 'w', newline='',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Наименование', 'Стоимость'])
            for card in cards:
                writer.writerow([card['title'], card['price']])
                print(f'{k} {count}/{all_tovar_in_pages}')
                count += 1
        sleep(2)

    return print('GameOver')



if __name__ == '__main__':
    get_html(JSON_FILE)




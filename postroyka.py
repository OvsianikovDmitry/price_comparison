import requests
from bs4 import BeautifulSoup
import csv
import json
from time import sleep


HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
CSV = 'postroyka.csv'
JSON_FILE = 'data_postroyka/postroyka_all_category_links.json'

# url ="https://www.postroyka.by/catalog/"
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
#     name = i.text
#     print(link)
#     categ_link = f'https://www.postroyka.by{link}'
#     w_link[name]=categ_link

# with open ('data_postroyka/postroyka_all_category_links.json', 'w', encoding='utf-8') as file:
#     json.dump(w_link, file, indent=4, ensure_ascii=False)

def get_text(el):
    if not el:
        return ''
    return el.get_text(strip=True)



def get_html(j_file):
    with open(j_file, encoding='utf-8') as file:
        category = json.load(file)
    count=0
    for k,v in category.items():

        url = v
        req = requests.get(url,headers=HEADERS)
        req.encoding='utf-8'
        res =req.text
        soup = BeautifulSoup(res, 'lxml')

        items = soup.find_all('div', class_='default_product')

        cards = []
        print('GET CONTENT')
        for i in items:
            cards.append({
                'title': i.find('div', class_='item').get_text(strip=True),
                'price': get_text(i.find('div', class_='basePrice'))
            })
        with open(f'data_postroyka/{k}.csv', 'w', newline='',encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Наименование', 'Стоимость'])
            for card in cards:
                writer.writerow([card['title'], card['price']])
                print('SAVE')
        sleep(2)

    return print('GameOver')




def get_content(res):
    soup = BeautifulSoup(res, 'lxml')

    items = soup.find_all('div', class_='default_product')

    cards =[]
    print('GET CONTENT')
    for i in items:
        cards.append({
            'title': i.find('div', class_='item').get_text(strip=True),
            'price': i.find('div', class_='basePrice').get_text(strip=True)
        })
    return cards



def save_doc(cards,path):
    with open(path,'w',newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Наименование','Стоимость'])
        for card in cards:
            writer.writerow([card['title'],card['price']])
            print("SAVE")


if __name__ == '__main__':
    get_html(JSON_FILE)
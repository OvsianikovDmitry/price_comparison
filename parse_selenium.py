from time import sleep
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import csv


j_file = 'all_categories_starstroi_new.json'

def get_data(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

def get_data_with_selenium(url):

    with open(j_file, encoding='utf-8') as file:
        category = json.load(file)

    for k,v in category.items():
        url = f'{v}'

        try:
            driver = webdriver.Chrome()
            driver.get(url=url)
            load_more=True
            while load_more:
                try:
                    more_tovarov =driver.find_element(By.CLASS_NAME,"products__load-more ")
                    more_tovarov.click()
                    sleep(random.randint(0,2))

                except Exception:
                    load_more=False

            page = driver.page_source
            soup = BeautifulSoup(page, 'lxml')
            all_links = soup.find_all('a', class_='product-card__see-more btn-prime')

            product = {}

            for i in all_links:
                url_for_parsing = "https://startstroi.by"+i.get('href')
                # print((url_for_parsing))
                product_str = ''
                est = 'В корзину'
                try:
                    # driver = webdriver.Chrome()
                    driver.get(url=url_for_parsing)
                    tovar_var = driver.find_elements(By.CLASS_NAME,"product__variation")
                    tovar_name = driver.find_element(By.CLASS_NAME,"product__title-info").text
                    for i in tovar_var:
                        tovar_price = driver.find_element(By.CLASS_NAME, "product__price")
                        tovar_nalichie = driver.find_element(By.NAME,"add-to-cart")
                        # print(tovar_nalichie.text)
                        # print(i.text)
                        sleep(random.randint(0,1))
                        i.click()
                        # print(tovar_price.text)
                        product_str = tovar_name+' '+i.text+' '+tovar_price.text+' '+tovar_nalichie.text
                        # print(product_str)
                        if est in product_str:
                            product[tovar_name+' '+i.text]=tovar_price.text


                except Exception as ex:
                    print(ex)

            with open(f'{k}.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['Наименование', 'Стоимость'])
                for key,val in product.items():
                    writer.writerow([key,val])
                    print('SAVE')
            sleep(2)



        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()






def main():
    # get_data()
    get_data_with_selenium(j_file)



if __name__ == '__main__':
    main()

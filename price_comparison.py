import csv
import re
from Book.parsing.select_category import *
from Book.parsing.dicts_products import *


def min_price(dict_tovar):
    type_t = type_p().casefold()
    thikness = thikness_gk()
    leight = leight_gk()

    new_dict = {}

    for k,v in dict_tovar.items():
        search_key = k.casefold()
        if type_t in search_key:
            if thikness[2] in search_key or thikness[1] in search_key:
                                if leight[0] in search_key or leight[1] in search_key or leight[2] in search_key or leight[3] in search_key:
                                    price = tovar_price(search_key)
                                    new_dict[search_key] = price


    for k,v in new_dict.items():
        if v == min(new_dict.values()):
            print(k,v)
            print('='*200)
    all_product(new_dict)

def all_product(dict_tovar):
    sort_val = sorted(dict_tovar.items(),key=lambda item: item[1])
    for i in sort_val:
        print(i)

def tovar_price(product):

    name_price =''

    for i in product:
        if i.isdigit():
            name_price += i
            price_1 = name_price[-4:-2] + '.' + name_price[-2:]
            price = float(price_1)

    return price



def price_profil(product):
    name_price = ''
    prof_price = product[-16:]
    price = 0
    for i in prof_price:
        if i.isdigit():
            name_price += i
    if len(name_price) == 1:
        price = int(name_price)
    elif len(name_price)>4:
        price_1 = name_price[-3] + '.' + name_price[-2:]
        price = float(price_1)
    else:
        price_1 = name_price[-4:-2] + '.' + name_price[-2:]
        price = float(price_1)

    return price



def price_samorez(product):

    name_price = ''
    price_reg = ' '
    prof_price = product[-14:]
    price = 0

    x = re.search(r'\d{1,3}[.,]\d{1,2}\w{3}',prof_price)
    if x:
        price_reg = x.group()
    else:
        x = re.search(r'\d{2}\w{3}', prof_price)
        if x:
            price_reg = x.group()

    for i in price_reg:
        if i.isdigit():
            name_price += i



    if len(name_price) <= 2:
        price = int(name_price)

    elif len(name_price)== 3:
        price_1 = name_price[-3] + '.' + name_price[-2:]
        price = float(price_1)

    elif len(name_price)== 5:
        price_1 = name_price[-5:-2] + '.' + name_price[-2:]
        price = float(price_1)

    else:
        price_1 = name_price[-4:-2] + '.' + name_price[-2:]
        price = float(price_1)

    return price

def vol_grunt_1(string):
    x = re.search(r'[1]\s[кгл]', string)
    if x:
        return x
    x_1  = re.search(r'[1][кгл]', string)
    if x:
        return x_1

def vol_grunt_2(string):
    x = re.search(r'[2]\s[кгл]', string)
    if x:
        return x
    x_1  = re.search(r'[2][кгл]', string)
    if x:
        return x_1

def vol_grunt_5(string):
    x = re.search(r'[5]\s[кгл]', string)
    if x:
        return x
    x_1  = re.search(r'[5][кгл]', string)
    if x:
        return x_1

def vol_grunt_10(string):
    x = re.search(r'[1][0]\s[кгл]', string)
    if x:
        return x
    x_1  = re.search(r'[1][0][кгл]', string)
    if x:
        return x_1

def vol_grunt_kraska_1_3(string):
    x = re.search(r'[1,3]\s[кгл]', string)
    if x:
        return x
    x_1 = re.search(r'[1,3][кгл]', string)
    if x:
        return x_1

def vol_grunt_kraska_4_5(string):
    x = re.search(r'\D[^.,12][4-5]\s[кгл]', string)
    if x:
        return x
    x_1 = re.search(r'\D[^,.12][4-5][кгл]', string)
    if x:
        return x_1

def vol_grunt_kraska_10(string):
    x = re.search(r'[1][0]\s[кгл]', string)
    if x:
        return x
    x_1 = re.search(r'[1][0][кгл]', string)
    if x:
        return x_1

def vol_grunt_kraska_15(string):
    x = re.search(r'[1-3][05]\s[кг]', string)
    if x:
        return x
    x_1 = re.search(r'[1-3][05][кг]', string)
    if x:
        return x_1

def vol_betonkontakt_4(string):
    x = re.search(r'[2-4]\s[кгл]', string)
    if x:
        return x
    x_1 = re.search(r'[2-4][кгл]', string)
    if x:
        return x_1

def vol_betonkontakt_7(string):
    x = re.search(r'\D[5-8]\s[кгл]', string)
    if x:
        return x
    x_1 = re.search(r'\D[5-8][кгл]', string)
    if x:
        return x_1

def vol_betonkontakt_15(string):
    x = re.search(r'[12][0-5]\s[кгл]', string)
    if x:
        return x
    x_1 = re.search(r'[12][0-5][кгл]', string)
    if x:
        return x_1

def compare_str(file):
    list_str = []
    for i in file:
        try:
            if len(i) == 1:
                tovar_name = i[0]
            elif len(i) == 2:
                tovar_name = i[0] +' '+ i[1]
            elif len(i) == 3:
                tovar_name = i[0] +' '+ i[1] +' '+ i[2]
            # print(tovar_name)
            list_str.append(tovar_name)
        except Exception as ex:
            print('FALE')

    return list_str

def shpatlevka_do_10(string):
    x = re.search(r'\D[1-9]\s[кг]', string)
    if x:
        return x
    x_1 = re.search(r'\D[1-9][кг]', string)
    if x:
        return x_1

def shpatlevka_15_20(string):
    x = re.search(r'[1][5-9]\s[кг]', string)
    if x:
        return x
    x_1 = re.search(r'[1][5-9][кг]', string)
    if x:
        return x_1

def shpatlevka_20(string):
    x = re.search(r'[23][0-9]\s[кг]', string)
    if x:
        return x
    x_1 = re.search(r'[23][0-9][кг]', string)
    if x:
        return x_1

def price_decorativa(product):

    name_price = ''
    price_reg = ' '
    prof_price = product[-15:]
    price = 0

    x = re.search(r'\d{2,3}[.,]\d{1,2}\w{3}',prof_price)
    if x:
        price_reg = x.group()
    else:
        x = re.search(r'\d{2,3}\w{3}', prof_price)
        if x:
            price_reg = x.group()

    for i in price_reg:
        if i.isdigit() :
            name_price += i

    if len(name_price)== 6:
        price_1 = name_price[-4:-2] + '.' + name_price[-2:]
        price = float(price_1)

    elif len(name_price) == 3:
        price_1 = name_price[1:]
        price = float(price_1)

    elif len(name_price)== 5:
        price_1 = name_price[-5:-2] + '.' + name_price[-2:]
        price = float(price_1)

    else:
        price_1 = name_price[-4:-2] + '.' + name_price[-2:]
        price = float(price_1)

    return price


def price_steklosetki(product):

    prof_price = product[-18:]
    price = 0


    x = re.search(r'\d{1,3}[.,]\d{1,2}\s[р]', prof_price)
    if x:
        price_reg = x.group()
        name_price = ''
        for i in price_reg:
            if not i.isalpha():
                name_price += i
                price = name_price.strip().replace(',', '.')

        return price
    else:
        x = re.search(r'\d{1,3}[.,]\d{1,2}[р]', prof_price)
        if x:
            price_reg = x.group()
            name_price = ''
            for i in price_reg:
                if not i.isalpha():
                    name_price += i
                    price = name_price.strip().replace(',', '.')

            return price
        else:
            x = re.search(r'\d{1,3}\s[р]', prof_price)
            if x:
                price_reg = x.group()
                name_price = ''
                for i in price_reg:
                    if not i.isalpha():
                        name_price += i
                        price = name_price.strip().replace(',', '.')

                return price
            else:
                x = re.search(r'\d{1,3}[р]', prof_price)
                if x:
                    price_reg = x.group()
                    name_price = ''
                    for i in price_reg:
                        if not i.isalpha():
                            name_price += i
                            price = name_price.strip().replace(',', '.')

                    return price




def open_list(file):
    with open(file,encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ';')
        tovar = compare_str(reader)

    return tovar







if __name__ == '__main__':
    f = select_cat()
    print('='*200)
    # price_samorez('Защита от плесени GOLDBASTIK BL 44 (концентрат 1:10) 1 л47.02 руб.')



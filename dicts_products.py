

def choice_tov(dict):
    for k, v in dict.items():
        print(k, v)

def tovar_name():
    tovar = {
        1: 'Гипсокартон',
        2: 'Гипсоволокнистый лист',
        3: 'Элемент пола'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите наименование'))
    return tovar.get(name_product)

def leight_gk():

    leight = {
        1:['1500','150'],
        2:['2000','200'],
        3:['2500','250'],
        4:['2750','275'],
        5:['3000','300']
    }
    choice_tov(leight)
    leight_prod = int(input('Какая нужна длина '))
    return leight.get(leight_prod)

def thikness_gk():

    thikness = {
        1:['Стеновой','12,5','12.5'],
        2:['Потолочный','9.5','9,5'],
        3:['Арочный','6.5','6,5']

    }

    choice_tov(thikness)
    type_p = int(input('Для каких целей'))
    return thikness.get(type_p)


def type_p():
    type_prod = {
        1:'Обычный',
        2:'Влагостойкий',
        3:'Огнестойкий'
    }
    choice_tov(type_prod)
    type_product = int(input('Какой тип'))
    return type_prod.get(type_product)

def thikness_gipsovolokno():
    thikness = {
        1: ['12,5','12.5'],
        2: ['10', '10.0'],
    }

    choice_tov(thikness)
    type_p = int(input('Для каких целей'))
    return thikness.get(type_p)


def leight_gipsovolokno():
    leight = {
        1: ['2500', '250'],
        2: ['1200', '120'],
    }
    choice_tov(leight)
    leight_prod = int(input('Какая нужна длина '))
    return leight.get(leight_prod)

def thikness_superpol():
    thikness = {
        1: ['20'],
    }

    choice_tov(thikness)
    type_p = int(input('Для каких целей'))
    return thikness.get(type_p)


def tovar_name_profil():
    tovar = {
        1: 'UD 27x28',
        2: 'CD 27x60',
        3: 'UW 50x40',
        4: 'CW 50x50',
        5: 'UV 75x40',
        6: 'UC 75x50',
        7: 'ПН 100x40',
        8: 'ПС 100x50',
        9: 'Усиленный для проемов 50x40',
        10:'Усиленный для проемов 75x40',
        11:'Усиленный для проемов 100x40',
    }
    choice_tov(tovar)
    name_product = int(input('Выберите наименование'))
    return tovar.get(name_product)

def krepej_profil():
    tovar = {
        1: 'Краб',
        2: 'Подвес удлинённый',
        3: 'Подвес прямой',
        4: 'Нониус',
        5: 'Соединитель',
    }
    choice_tov(tovar)
    name_product = int(input('Выберите наименование'))
    return tovar.get(name_product)

def samorezi_and_dubeli():
    tovar = {
        1: 'Саморез до 16 мм',
        2: 'Саморез от 17 до 25 мм',
        3: 'Саморез от 30 до 40 мм',
        4: 'Саморез от 40 до 50 мм',
        5: 'Саморез от 50 до 60 мм',
        6: 'Саморез от 60 до 70 мм',
        7: 'Саморез от 70 до 80 мм',
        8: 'Саморез от 80 до 90 мм',
        9: 'Саморез свыше 90 мм',
        10: 'Дюбель-гвоздь длина 40 мм',
        11: 'Дюбель-гвоздь длина 60 мм',
        12: 'Дюбель-гвоздь длина 80 мм',
        13: 'Дюбель для теплоизоляции',
    }
    choice_tov(tovar)
    name_product = int(input('Выберите наименование'))
    return tovar.get(name_product)

def grunt_kraska():
    tovar = {
        1:'Грунт глубокого проникновения',
        2:'Грунт-краска',
        3:'Бетон-контакт'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите наименование'))
    return tovar.get(name_product)

def volume_grunt():
    tovar = {
        1: '1л',
        2: '2л',
        3: '5л',
        4: '10л'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите объём'))
    return tovar.get(name_product)

def volume_grunt_kraska():
    tovar = {
        1: '1-3',
        2: '4-5',
        3: '10',
        4: '15+'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите объём'))
    return tovar.get(name_product)

def volume_beton_kontakt():
    tovar = {
        1: 'до 4 кг',
        2: '7,5 кг',
        3: '15 кг'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите объём'))
    return tovar.get(name_product)

def shpatlevka_type():
    tovar = {
        1: 'Готовая в вёдрах',
        2: 'В мешках',
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)

def shpatlevka_vol():
    tovar = {
        1: 'до 10 кг',
        2: '15-20 кг',
        3: 'свыше 20'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите объём'))
    return tovar.get(name_product)


def shpatlevka_meshok():
    tovar = {
        1: 'Цементная',
        2: 'Гипсовая,Полимерная',
        3: 'Для швов'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)

def shtukaturka_type():
    tovar = {
        1: 'Цементная',
        2: 'Гипсовая',
        3: 'Декоративная'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип штукатурки'))
    return tovar.get(name_product)

def steklosetka_list():
    tovar = {
        1: 'Сетка штукатурная',
        2: 'Стеклохолст малярный',
        3: 'Сетка сварная'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип сетки'))
    return tovar.get(name_product)

def lenti_ugly():
    tovar = {
        1: 'Ленты для стыков',
        2: 'Ленты для углов',
        3: 'Уголки перфорированные'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)

def smesi_pola():
    tovar = {
        1: 'Стяжка',
        2: 'Самонивелир',
        3: 'Песок, щебень, керамзит, фибра',
        4: 'Лента демпферная',
        5: 'Цемент'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)

def utepliteli_type():
    tovar = {
        1: 'Пенопласт',
        2: 'Экструдированный пенополистирол',
        3: 'Рулонный утеплитель',
        4: 'Утеплитель в плитах'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)

def uteplitel_plita_rulon_tolschina():
    tovar = {
        1: '50 мм',
        2: '100 мм',
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)

def penoplast_tolshina():
    tovar = {
        1: '20 мм',
        2: '30 мм',
        3: '50 мм',
        4: '100 мм'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)

def extrudirovani():
    tovar = {
        1: '20 мм',
        2: '30 мм',
        3: '40 мм',
        4: '50 мм',
        5: '60 мм',
        6: '80 мм',
        7: '100 мм'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)

def type_uteplitel_v_plitah():
    tovar = {
        1: 'Для фасада',
        2: 'Тепло-звуко изоляция',
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)

def germetiki_i_silikon():
    tovar = {
        1: 'Акриловый герметик',
        2: 'Силиконовый герметик',
        3: 'Клей-ГЕРМЕТИК',
        4: 'Клей-Шпатлёвка',
        5: 'Кровельные,высокотемпературные,виброакустические',
        6: 'Для дерева(цветные)'
    }
    choice_tov(tovar)
    name_product = int(input('Выберите тип'))
    return tovar.get(name_product)
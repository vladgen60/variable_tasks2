data = int(input('Введите число вашего рождения: '))
sign = input('Введите месяц вашего рождения: ')

if 31 >= data >= 22 and sign == 'декабрь' or 19 >= data >= 1 and sign == 'январь':
    print('Козерог')
if 31 >= data >= 20 and sign == 'январь' or 18 >= data >= 1 and sign == 'февраль':
    print('Водолей')
if 28 >= data >= 19 and sign == 'февраль' or 20 >= data >= 1 and sign == 'март':
    print('Рыбы')
if 31 >= data >= 20 and sign == 'март' or 19 >= data >= 1 and sign == 'апрель':
    print('Овен')
if 30 >= data >= 20 and sign == 'апрель' or 20 >= data >= 1 and sign == 'май':
    print('Телец')
if 31 >= data >= 21 and sign == 'май' or 20 >= data >= 1 and sign == 'июнь':
    print('Близнецы')
if 31 >= data >= 21 and sign == 'июнь' or 22 >= data >= 1 and sign == 'июль':
    print('Рак')
if 30 >= data >= 23 and sign == 'июль' or 22 >= data >= 1 and sign == 'август':
    print('Лев')
if 31 >= data >= 23 and sign == 'август' or 22 >= data >= 1 and sign == 'сентябрь':
    print('Дева')
if 30 >= data >= 21 and sign == 'сентябрь' or 22 >= data >= 1 and sign == 'октябрь':
    print('Весы')
if 31 >= data >= 23 and sign == 'октябрь' or 21 >= data >= 1 and sign == 'ноябрь':
    print('Скорпион')
if 30 >= data >= 22 and sign == 'ноябрь' or 2119 >= data >= 1 and sign == 'декабрь':
    print('стрелец')

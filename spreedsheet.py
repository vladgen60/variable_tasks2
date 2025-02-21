price_low = float(input('Введите цену со скидкой: '))
price_list = []
price_list.append(price_low)
for i in range(len(price_list)):
    high_price = price_low * 100 / 60
    print('Старая цена: {0:5.2f}'.format(high_price))
    print('Новая цена: {0:6.2f}'.format(price_low))
    print(f'Ваша выгода: {(high_price - price_low):5.2f}')


price_list = [4.95, 9.95, 14.95, 19.95, 24.95]
n = 1

for i in range(len(price_list) + 1):
    high_price = price_list[i] * 100 / 60
    print(f'Товар №{n}')
    print('Старая цена: {0:5.2f}'.format(high_price) + '$')
    print('Новая цена: {0:6.2f}'.format(price_list[i]) + '$')
    print(f'Ваша выгода: {(high_price - price_list[i]):5.2f}' + '$')
    print()
    
    n += 1

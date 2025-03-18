my_fruits = {'apple': 4.95, 'limon': 9.95, 'pear': 49.95, 'grape': 19.95, 'banana': 24.95}
old_price = []
old_key = []
dif_prices = []
for key in my_fruits:
   value_old = int(100 *  my_fruits[key] / 40)
   dif_price = value_old - my_fruits[key]
   dif_prices.append(dif_price)
   old_price.append(value_old)
   old_key.append(key)
print(my_fruits.keys())
y = old_key
x = old_price
z = dict(zip(y, x))
k = dif_prices

# print(f'Новые цены: {my_fruits}')
# print(f'Разница цен: {k}')


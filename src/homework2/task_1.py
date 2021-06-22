rub = int(input('Количетсво рублей: '))
penny = int(input('Количетсво копеек: '))
count = int(input('Количество товаров: '))
price = (rub * 100 + penny) * count
price_rub = price // 100
price_pen = price % 100
print('Общая стоимость: ', str(price_rub) + ' руб.', str(price_pen) + ' коп.')

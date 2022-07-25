#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампы -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


table_code = goods['Стол']
table_quantity = store[table_code][0]['quantity'] + store[table_code][1]['quantity']
table_cost_1 = store[table_code][0]['quantity'] * store[table_code][0]['price']
table_cost_2 = store[table_code][1]['quantity'] * store[table_code][1]['price']
common_table_cost = table_cost_1 + table_cost_2
print('Столы -', table_quantity, 'шт, стоимость', common_table_cost, 'руб')

fotel_code = goods['Диван']
fotel_quantity = store[fotel_code][0]['quantity'] + store[fotel_code][1]['quantity']
fotel_cost_1 = store[fotel_code][0]['quantity'] * store[fotel_code][0]['price']
fotel_cost_2 = store[fotel_code][1]['quantity'] * store[fotel_code][1]['price']
common_fotel_cost = fotel_cost_1 + fotel_cost_2
print('Диваны -', fotel_quantity, 'шт, стоимость', common_fotel_cost, 'руб')

chair_code = goods['Стул']
chair_quantity = store[chair_code][0]['quantity'] + store[chair_code][1]['quantity'] + store[chair_code][2]['quantity']
chair_cost_1 = store[chair_code][0]['quantity'] * store[chair_code][0]['price']
chair_cost_2 = store[chair_code][1]['quantity'] * store[chair_code][1]['price']
chair_cost_3 = store[chair_code][2]['quantity'] * store[chair_code][2]['price']
common_chair_cost = chair_cost_1 + chair_cost_2 + chair_cost_3
print('Стулья -', chair_quantity, 'шт, стоимость', common_chair_cost, 'руб')

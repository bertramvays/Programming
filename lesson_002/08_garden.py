#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)


# выведите на консоль все виды цветов
flowers = garden_set | meadow_set
print('Все цветы', flowers)

# выведите на консоль те, которые растут и там и там
common_flowers = garden_set & meadow_set
print("Цветы которые растут и там и там: ", common_flowers)


only_meadow_flowers = meadow_set - garden_set
print(meadow_set, garden_set)
print('Цветы которые растут только на лугу: ', only_meadow_flowers)

# выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden_flowers = garden_set - meadow_set
print('Цветы которые растут только в саду: ', only_garden_flowers)

# выведите на консоль те, которые растут на лугу, но не растут в саду


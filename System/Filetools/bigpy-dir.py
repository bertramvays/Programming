"""
Отыскивает наибольший файл с исходным программным кодом на языке Пайтон в единственном
каталоге. Поиск выполняется в каталоге стандартной библиотеки Пайтон, если в аргументе
командной строки не был указан какой-то другой каталог.
"""
import os, glob, sys

dirname = r'/lib/python3.9'
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])

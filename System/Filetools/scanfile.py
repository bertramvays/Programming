"""
Определим универсальную процедуру сканирования файлов, которая просто применяет
переданную ей функцию к каждой строке внешнего файла.
"""


def scanner(name, function):
    file = open(name, 'r')  # создать объект файла
    while True:
        line = file.readline()  # вызов метода файла
        if not line: break
        function(line)  # вызываем объект функции
    file.close()

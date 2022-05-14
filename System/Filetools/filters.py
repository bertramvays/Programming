import sys


def filter_files(name, function):  # фильтрация файлов через функцию
    input = open(name, 'r')  # создать объекты файлов
    оutput = open(name + '.out', 'w')  # выходной файл
    for line in input:
        output.write(function(line))  # записать измененную строку
    input.close()
    output.close()


def filter_stream(function):  # отсутствуют явные файлы
    while True:               # использовать стандартные потоки
        line = sys.stdin.readline()  # или: input()
        if not line: break
        print(function(line), end='')  # или sys.stdout.write()


if __name__ == '__main__':
    filter_stream(lambda line: line)  # копировать stdin stdout, если запущен как сценар
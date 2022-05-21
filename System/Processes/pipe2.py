# аналогичен сценарию pipe1.py, но обертывает входной дескриптор канала
# объектом файла для обеспечения построчного чтения данных,
# и в обоих процессах закрывает неиспользуемый дескриптор канала
import os, time


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)  # заставить родителя подождать
        msg = ('Spam %03d\n' % zzz).encode()  # каналы двоичные файлы
        os.write(pipeout, msg)  # отправить данные родителю
        zzz = (zzz+1) % 5  # переход к 0 после 4


def parent():
    pipein, pipeout = os.pipe()  # создать канал с 2-мя концами
    if os.fork() == 0:
        os.close(pipein)  # закрить дескриптор ввода
        child(pipeout)  # в копии вызвать child
    else:                  # в родителе слушать канал
        os.close(pipeout)  # закрыть дескриптор вывода
        pipein = os.fdopen(pipein)  # создать объект текстового файла
        while True:
            line = pipein.readline()[:-1]  # остановиться до получения данных
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


parent()

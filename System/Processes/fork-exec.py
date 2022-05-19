"""
 Запускает программы пока не будет нажата кнопка 'q'.
 """


import os


parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:                                               # копия процесса
        os.execlp('python', 'python', 'child.py', str(parm))   # подменить прогр.
        assert False, 'error starting program'  # возврата бить не должно

    else:
        print('Child is', pid)
        if input() == 'q': break

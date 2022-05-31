import sys
from tkinter import *

def hello(event):
    print('Press twice to exit')  # одиночный щелчок левой кнопкой


def quit1(event):  # собственный обработчик событий
    print("Hello, I myst be going...") # event ет виджет, координаты и т.д.
    sys.exit()  # закрить окно и завершить процесс


widget = Button(None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)  # привязать обработчик щелчка
widget.bind('<Double-1>', quit)  # привязать обработчик двойного щелчка
widget.mainloop()


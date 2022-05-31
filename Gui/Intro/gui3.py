import sys
from tkinter import *


def quit1(msg):  # собственный обработчик событий
    print(msg)
    sys.exit()  # закрить окно и завершить процесс


widget = Button(None, text='Hello event world', command=quit1('Hello, I must be going...'))
widget.pack()
widget.mainloop()

import sys
from tkinter import *


class HelloClass:
    def __init__(self):
        widget = Button(None, text='Hello event world', command=self.quit)
        widget.pack()


    def quit(self):
        print("Hello class method world")  # self.quit = связанный метод хранит пару
        sys.exit()  # self + quit

HelloClass()
mainloop()

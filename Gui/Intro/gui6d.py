from tkinter import *
from gui6 import Hello


class HelloExtender(Hello):
    def make_widgets(self):  # сширение метода
        Hello.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)

    def message(self):
        print('Hello', self.data)  # переопределение метода


if __name__ == '__main__': HelloExtender().mainloop()

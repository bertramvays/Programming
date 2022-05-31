from tkinter import *


class HelloButton(Button):
    def __init__(self, parent=None, **config):  # регистрирует метод callback
        Button.__init__(self, parent, **config)  # и добавляет себя в интерфейс
        self.pack()  # можно использовать старый стиль аргумента config
        self.config(command=self.callback)

    def callback(self):  # действие при нажатии
        print('Goodbye world...')  # переопределить в подклассах
        self.quit()


if __name__ == '__main__':
    HelloButton(text='Hello subclass world').mainloop()

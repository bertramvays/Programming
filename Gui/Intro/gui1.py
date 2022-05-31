from tkinter import Label  # ипортировать виджет


widget = Label(None, text='Hello GUI world!')  # создать его
widget.pack()  # разместить
widget.mainloop()  # запустить цикл событий

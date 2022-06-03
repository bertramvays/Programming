from tkinter import *

root = Tk()
labelfont = ('times', 12, 'bold')  # семейство, размер, стиль
widget = Label(root, text='Hello config world')
widget.config(bg='black', fg='yellow')  # желтый тескт на черном фоне
widget.config(font=labelfont)  # использовать увеличенный шрифт
widget.config(height=3, width=20)  # начальный размер: строк, символов
widget.config(cursor='gumby')
widget.pack(expand=YES, fill=BOTH)
root.mainloop()

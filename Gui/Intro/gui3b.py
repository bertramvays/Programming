import sys
from tkinter import *  # lambda-выражение генерирует функцию


widget = Button(None, text='Hello event world',
                command=(lambda: print('Hello lambda world') or sys.exit()))
widget.pack()
widget.mainloop()

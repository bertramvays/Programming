from tkinter import *

root = Tk()
Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES, fill=X)
Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES, fill=BOTH)
Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES, fill=X)
root.mainloop()

from tkinter import *

ws = Tk()
ws.title('PythonGuides')


img = PhotoImage(file='images/sasuke.png')
Label(
    ws,
    image=img
).pack()

ws.mainloop()

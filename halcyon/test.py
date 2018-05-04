import tkinter as tk
from planet import Planet

hoth = Planet('Hoth', 10, 10)

root = tk.Tk()

root.geometry('300x300')
w = tk.Label(root, text=hoth)
z = tk.Label(root, text='at %d, %d' % (hoth.x_pos, hoth.y_pos))
w.pack()
z.pack()

root.mainloop()

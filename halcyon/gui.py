from tkinter import *

root = Tk()
root.geometry('1250x750')
root.title('Halcyon')

celestial_view = Frame(root, height=500, width=200, bd=2, relief=SUNKEN, bg='red')
celestial_view.pack(padx=5, pady=5, side=LEFT)

player_view = Frame(root, height=500, width=200, bd=2, relief=SUNKEN, bg='green')
player_view.pack(padx=5, pady=5, side=RIGHT)

zone_view = Frame(root, height=500, width=1000, bd=2, relief=SUNKEN, bg='purple')
zone_view.pack(padx=5, pady=5)

mainloop()

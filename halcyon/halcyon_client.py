import tkinter as tk
from task import ACTIVE_TASKS, Task

def make_display_list(list):
    #takes a list of items and splits them up into a string
    #where each item is on a newline
    temp_text = ''
    for item in list:
        if item != list[-1]:
            temp_text += str(item) + '\n'
        else:
            temp_text += str(item)
    return temp_text

class HalcyonClient(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, new_frame_class):
        new_frame = new_frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()

class LoginPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        loginlabel = tk.Label(self, text='Enter your player name.')
        loginlabel.pack()
        loginentry = tk.Entry(self)
        loginentry.pack()
        loginbutton = tk.Button(self, text='Login')
        loginbutton.pack()

a = HalcyonClient()

a.mainloop()

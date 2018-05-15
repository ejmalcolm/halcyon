from tkinter import *
from task import ACTIVE_TASKS, Task

root = Tk()
root.geometry('1250x750')
root.title('Halcyon -- Client')


celestial_view = Frame(root, height=500, width=200, bd=2, relief=SUNKEN, bg='red')
celestial_view.pack(padx=5, pady=5, side=LEFT)

player_view = Frame(root, height=500, width=200, bd=2, relief=SUNKEN, bg='green')
player_view.pack(padx=5, pady=5, side=RIGHT)

zone_view = Frame(root, height=500, width=1000, bd=2, relief=SUNKEN, bg='purple')
zone_view.pack(padx=5, pady=5)

alert_view = Frame(root, height=100, width=600, bd=2, relief=SUNKEN, bg='orange')
alert_view.pack(padx=5, pady=5)

task_view = Frame(root, height=100, width=600, bd=2, relief=SUNKEN, bg='cyan')
task_view.pack(padx=5, pady=5)

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

abc = Task(1, make_display_list)
efg = Task(2, make_display_list, result='make a building')

task_text = make_display_list(ACTIVE_TASKS)
task_list = Message(task_view, text=task_text, bg='grey', width=600)
task_list.pack()

mainloop()

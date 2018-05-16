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

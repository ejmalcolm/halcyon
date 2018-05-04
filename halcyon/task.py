ACTIVE_TASKS = []

class Task():
    
    def __init__(self, time_needed, end_function):
        self.time_left = time_needed
        self.end_func = end_function
        
    def decrease_time(self, amount):
        self.time_left -= amount

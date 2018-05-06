from time import time, sleep

class Task():

    def __init__(self, hours_needed, end_func):
        #calculates the end_time and saves it as an attribute
        #time() gets a relative number of seconds since the epoch
        #then, the number of hours (time_needed) is converted to seconds
        #the end time is set to the current time + the time needed
        self.end_time = time() + (hours_needed*3600)
        self.end_func = end_func

    def check_progress(self):
        print('called')
        #if the end time has passed, call end_func())
        if self.end_time <= time():
            print('The task was finished.')
            self.end_func()
            return True
        #otherwise, report the hours/minutes left until its done
        seconds_left = self.end_time - time()
        if seconds_left >= 3600:
            hours_left = int((seconds_left/3600))
            print('there are %s hours remaining' % hours_left)
            return False
        else:
            minutes_left = int((seconds_left/60))
            print('there are %s minutes left' % minutes_left)
        return False

##this is the function to start a loop to check and update a task every 5 minutes
def task_loop(task):
    while True:
        try:
            #replace task with the reference of the Task() to check
            task.check_progress()
            sleep(300)
        except KeyboardInterrupt:
            raise

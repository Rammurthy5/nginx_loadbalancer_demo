import time
from .tasks import process_stuff_task

def process_stuff():
    return process_stuff_task.delay()
    
'''
def process_stuff_actual():
    print("processing stuff ")
    start = time.asctime()
    time.sleep(30)
    return "Start {} Current timestamp {}".format(start, time.asctime())
'''

import time 


def process_stuff_actual():
    print("processing stuff ")
    start = time.asctime()
    time.sleep(30)
    return "Start {} Current timestamp {}".format(start, time.asctime())


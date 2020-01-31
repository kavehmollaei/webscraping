import threading
import os
import time
import datetime


def task1():
    print('Start time:{}]\n' .format(datetime.datetime.now()))
    print('Currnet Thread name is {} and the process ID is {}\n'.format(threading.current_thread().name,os.getpid()))

def task2():
    print('Start time:{}]\n' .format(datetime.datetime.now()))
    print('Currnet Thread name is {} and the process ID is {}\n'.format(threading.current_thread().name,os.getpid()))



print('start time:{}]\n' .format(datetime.datetime.now()))
print('Main Thread name is {} and the process ID is {}\n'.format(threading.main_thread().name,os.getpid()))
t1  = threading.Thread(target=task1 , name='T1')
t2 = threading.Thread(target=task2 , name='T2')

t1.start()
t2.start()


t1.join()
t2.join()
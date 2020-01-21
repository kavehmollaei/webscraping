import requests
import threading
import time
import datetime
import os
def thr1():

    url = 'https://www.digikala.com/'
    for i in range(0,4):

        r = requests.get(url)
        print(r.status_code)
        print('Start time:{}]\n' .format(datetime.datetime.now()))
        print('Currnet Thread name is {} and the process ID is {}\n'.format(threading.current_thread().name,os.getpid()))
        print(threading.active_count())
            

def thr2():
    url = 'https://www.digikala.com/'
    for i in range(0,4):

        r = requests.get(url)
        print(r.status_code)
        print('Start time:{}]\n' .format(datetime.datetime.now()))
        print('Currnet Thread name is {} and the process ID is {}\n'.format(threading.current_thread().name,os.getpid()))
        print(threading.active_count())


print('start time:{}]\n' .format(datetime.datetime.now()))
print('Main Thread name is {} and the process ID is {}\n'.format(threading.main_thread().name,os.getpid()))
t1=threading.Thread(target=thr1 , name='T1') 
t2=threading.Thread(target=thr2 , name='T2')  
print(threading.active_count())


t1.start() 
t2.start()

t1.join()
t2.join()
import threading
import time


def task1():
    for i in range(5):
        #current_process()获取进程信息
        print(threading.current_thread().name,f"task1---{i}")
        time.sleep(1)

def task2():
    for i in range(5):
        print(threading.current_thread().name,f"task2---{i}")
        time.sleep(1)

def task():
    t1 = threading.Thread(target=task1,name="1111")
    t2 = threading.Thread(target=task2,name="2222")
    t1.start()
    t2.start()
    print(threading.current_thread())

task()
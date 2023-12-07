import multiprocessing as mp
import os
import time


def task1(n,arg):
    for i in range(5):
        #current_process()获取进程信息
        print("11111",mp.current_process())
        print(mp.current_process().name)
        #os获取进程id、父进程id
        print("id",os.getpid(),os.getppid())
        #通过创建进程给方法传参
        print(n,arg)
        time.sleep(1)

def task2(num,s):
    for i in range(5):
        print("22222",mp.current_process())
        print(num,s)
        time.sleep(1)


def main(*args,**kwargs):
    p1 = mp.Process(target=task1,args=(2,"qwer"),name="myprocess1")
    p2 = mp.Process(target=task2,kwargs={"s":"qwer","num":3})
    print("test over1")
    p1.daemon=True
    p2.daemon=True
    print("test over2")
    print(*args)
    p1.start()
    p2.start()
    time.sleep(2)
    print("33333", mp.current_process())
if __name__ == '__main__':
    main(1,3,"1",23,q=2)
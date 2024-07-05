from threading import Thread
from time import sleep


def fun1(num):
    for i in range(num):
        print(f"A - {i}")
        sleep(.5)


def fun2(num, msg):
    for i in range(num):
        print(f"{msg} - {i}")
        sleep(.5)


t1 = Thread(target=fun1, args = (10,))
t2 = Thread(target=fun2, args = (10, "B"))
t1.start()
t2.start()

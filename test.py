#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' test '

__author__ = 'YUNEEC'

import decimal
import threading
import time

from Yuneec import Yuneec
from Yuneec import L


def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn


@metric
def foo():
    print("starting...")
    time.sleep(0.1)
    while True:
        res = yield 4
        print("res:", res)


def fun1():
    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))
    abs(-10)


def fun2():
    s1 = Student("lifei", 90)
    print(s1)


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score


def fun_timer():
    global count
    count = count + 1
    print('hello timer ', count)
    global timer
    # 重复构造定时器
    timer = threading.Timer(1, fun_timer)
    timer.start()
    if count == 5:
        timer.cancel()


if __name__ == '__main__':
    # fun2()
    # count = 0
    # timer = threading.Timer(1, fun_timer)
    # timer.start()
    # time.sleep(6)
    # print(count)
    number = 95895.221
    list = [95895.000, 95895.200, 95895.400, 95895.600, 95895.800]
    print("type(list):", type(list), " ,type(number):", type(number), ",number:", number)
    result = format(min(list, key=lambda x: abs(x - number)), '.3f')
    re = decimal.Decimal("%.3f" % float(number))
    print(re, ",type(re):", type(re))
    print("result:", result)

    y = Yuneec()
    y.printName()

    l = L()
    l.printName()

import datetime
import time

# gps = 1180344041
gps = 2134959071
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(gps)))

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

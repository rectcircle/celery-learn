# -*- coding: utf-8 -*-

from get_started.tasks1 import add


def product1():
    print "get_started 生产者 调用开始"
    result = add.delay(4, 4)
    print "get_started 生产这 调用结束"
    return result

# -*- coding: utf-8 -*-

from get_started.producer1 import product1
from celery.result import AsyncResult
from time import sleep


if __name__ == '__main__':
    # 配置了backend，返回的就是AsyncResult对象
    print "====测试使用backend===="
    task_result1 = product1()
    task_result2 = product1()
    print type(task_result1)
    print task_result1.task_id, task_result2.task_id
    print task_result1.backend, task_result2.backend

    while not task_result1.ready():
        sleep(.5)
    print task_result1.result
    while not task_result2.ready():
        sleep(.5)
    print task_result2.result

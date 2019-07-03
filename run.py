# -*- coding: utf-8 -*-

from get_started.producer import product
from celery.result import AsyncResult
from time import sleep


if __name__ == '__main__':
    # 不配置结果backend，将无法拿到结果
    print "====测试不使用backend===="
    task_result1 = product()
    task_result2 = product()
    print type(task_result1)
    print task_result1.task_id, task_result2.task_id
    print task_result1.backend, task_result2.backend

    # while not task_result1.ready():
    #     sleep(.5)
    # print task_result1.result
    # while not task_result2.ready():
    #     sleep(.5)
    # print task_result2.result

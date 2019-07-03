# -*- coding: utf-8 -*-

from celery import Celery
from time import sleep

app = Celery('tasks',
             broker='redis://localhost:6379/1',)


# 在此定义了一个任务
@app.task
def add(x, y):
    print "get_started 消费者开始执行"
    sleep(5)
    result = x + y
    print "get_started 消费者执行结束"
    return result

# 运行该任务： celery -A get_started.tasks worker --loglevel=info
# 并发度默认为cpu核心数

from celery import Celery

app = Celery('hello', broker='redis://localhost:6379/1')


@app.task
def hello():
    return 'hello world'

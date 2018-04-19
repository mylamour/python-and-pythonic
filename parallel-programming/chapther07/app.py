from math import sqrt
from celery import Celery

# celery -A app worker --loglevel=INFO
app = Celery('tasks', broker='redis://127.0.0.1:6379/0')

# @app.task
# def hello_world():
#     return "I am celery task"
@app.task
def square_root(value):
    return sqrt(value)

@app.task
def fibo_task(value):
    a, b = 0, 1
    for item in range(value):
        a, b = b, a + b

    message = "The Fibonacci calculated with task id %s was %d" %(fibo_task.request.id, a)
    return (value,message)

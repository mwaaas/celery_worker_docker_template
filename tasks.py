__author__ = 'Mwaaas'
__email__ = 'francismwangi152@gmail.com'
__phone_number__ = '+254702729654'


from celery import Celery

app = Celery('tasks', broker='amqp://guest@rabbitmq//')

@app.task
def add(x, y):
    return x + y
import random
import datetime

from celery import Celery, shared_task

from .bot import start_bot


app = Celery()


# @shared_task
# def hello():
#     print('Hello')
#     output = "Hello World"
#     return output

@shared_task
def create_user_list():
    start_bot()

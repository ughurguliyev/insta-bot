import random
import datetime

from celery import Celery, shared_task

from .bot import start_bot


app = Celery()

@shared_task
def create_user_list(instance):
    start_bot(title=instance)

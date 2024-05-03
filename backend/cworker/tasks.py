import time
from celery import shared_task


@shared_task
def tp0(queue='celery'):
    time.sleep(3)
    return


@shared_task
def tp1(queue='celery1'):
    time.sleep(3)
    return

@shared_task
def tp2(queue='celery2'):
    time.sleep(3)
    return

@shared_task
def tp3(queue='celery3'):
    time.sleep(3)
    return
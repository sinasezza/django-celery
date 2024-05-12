import time
from celery import shared_task
from django.core.management import call_command


@shared_task
def management_command():
    call_command("test_command")


# @shared_task
# def tp1(queue="celery1"):
#     time.sleep(3)
#     return


# @shared_task
# def tp2(queue="celery2"):
#     time.sleep(3)
#     return


# @shared_task
# def tp3(queue="celery3"):
#     time.sleep(3)
#     return

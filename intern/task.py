from celery import shared_task
from time import sleep


@shared_task
def send_mail():
    sleep(20)

from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.decorators import task
from celery.utils.log import get_task_logger

from .helper import process_stuff_actual

logger = get_task_logger(__name__)


@shared_task
def process_stuff_two():
    print("processing stuff ")
    start = time.asctime()
    time.sleep(30)
    return "Start {} Current timestamp {}".format(start, time.asctime())


@task(name="process_stuff_task")
def process_stuff_task():
    logger.info("Task successful")
    return process_stuff_actual()


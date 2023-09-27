from celery import shared_task
import time
from breachlock_proj.celery import *
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level as needed
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


@app.task(queue='addition', max_retries = 2 , default_retry_delay = 12)
def add(x, y):
    try:
        time.sleep(10)  # Sleep for 10 seconds to simulate work
        return f"The sum of {x} and {y} is {int(x)+int(y)}."
    except Exception as exc:
        add.retry(exc=exc, args=(x, y))
@app.task(queue='subtraction', max_retries = 2 , default_retry_delay = 12)
def subtract(x, y):
    try:
        time.sleep(10)  # Sleep for 10 seconds to simulate work
        return f"The abs subtraction of {x} and {y} is {abs(int(x)-int(y))}."
    except Exception as exc:
        raise subtract.retry(exc=exc, args=(x, y))

@app.task(queue='multiplication', max_retries = 2 , default_retry_delay = 12)
def multiply(x, y):
    try:
        time.sleep(10)  # Sleep for 10 seconds to simulate work
        return f"The multiplication of {x} and {y} is {int(x)*int(y)}."
    except Exception as exc:
        multiply.retry(exc=exc, args=(x, y))

#managing task which ultimately fail
from celery.signals import task_postrun
@task_postrun.connect
def handle_failed_task(sender=None, **kwargs):
    if kwargs.get('state') == 'FAILURE':
        task_name = kwargs.get('task').name
        exception = kwargs.get('retval') 
        task_id = kwargs.get('task_id')

        logger.error(f"Task '{task_name}' (ID: {task_id}) failed with exception: {exception}")
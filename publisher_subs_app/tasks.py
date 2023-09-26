from celery import shared_task
import time
from breachlock_proj.celery import *

@app.task(queue='addition')
def add(x, y):
    time.sleep(10)  # Sleep for 10 seconds to simulate work
    return f"The sum of {x} and {y} is {x+y}."

@app.task(queue='subtraction')
def subtract(x, y):
    time.sleep(10)  # Sleep for 10 seconds to simulate work
    return f"The abs subtraction of {x} and {y} is {x-y}."

@app.task(queue='multiplication')
def multiply(x, y):
    time.sleep(10)  # Sleep for 10 seconds to simulate work
    return f"The multiplication of {x} and {y} is {x*y}."
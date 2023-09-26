# breachlock_project
Event Driven Architecture using Django, Celery, RabbitMQ, Redis and PostgreSQL
Introduction
This Django project implements a simplified calculation tasks of addition, multiplication, subtraction to showcase Event Driven Architecture, using Celery, RabitMQ, Redis, PostgreSQL

The celery acts as a distributed task queue system  to handle asynchronous tasks. 
It allows you to offload time-consuming or resource-intensive tasks from your main application to background workers, making your application more responsive and scalable.

Rabbit MQ is used as a message broker and to store the tasks in the queues

Redis is used as a Celery backend to store the task status and results

PostgreSQL is used to store Task Ids and mapped with queue name

Libraries and Frameworks
Django: Used as the web framework.
Django REST Framework: Used for creating RESTful APIs.
PostgreSQL: Used as the database for storing data.
Celery 
Redis
Pika --> python handler for RabbitMQ

Setup Instructions
Clone this repository to your local machine.
Create a virtual environment: python -m venv venv.
Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS and Linux: source venv/bin/activate
Install project dependencies: pip install -r requirements.txt.
Set up the database and run migrations: python manage.py migrate.
Start the development server: python manage.py runserver
Also install RabbitMQ, Redis on your local machine as well and keep them running







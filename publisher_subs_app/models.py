from django.db import models

# Create your models here.
class CeleryTasks(models.Model):
	id = models.AutoField(primary_key=True)
	queue_name = models.CharField(max_length = 50)
	task_id = models.CharField(max_length = 300)
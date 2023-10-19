from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length= 20)
    taskDescription = models.CharField(max_length= 100)
    is_completed = models.BooleanField(default=False)
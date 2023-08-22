from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
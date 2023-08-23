from django.db import models

# Create your models here.
class rstudent(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    roll = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
from django.db import models


# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=20)
    sname = models.CharField(max_length=100)
    sage = models.CharField(max_length=10)
    scity = models.CharField(max_length=100)
    sclass = models.CharField(max_length=100)

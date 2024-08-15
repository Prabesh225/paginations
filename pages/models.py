from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    rolled = models.IntegerField()
    courses = models.CharField(max_length=50)
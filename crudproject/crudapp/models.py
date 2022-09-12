from django.db import models

# Create your models here.

class Student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=50)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.IntegerField()
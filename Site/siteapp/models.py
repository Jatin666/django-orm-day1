from django.db import models


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Student(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    marks = models.IntegerField()
    # if school gets deleted all things will be deleted.it is building a relation
    school = models.ForeignKey(School, on_delete=models.CASCADE)

from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Employee(models.Model):
    empid = models.CharField(max_length=10)
    empname = models.CharField(max_length=100)
    designation = models.CharField(max_length=20)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

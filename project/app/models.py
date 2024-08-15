from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    mark = models.IntegerField()
    def __str__(self):
        return self.name
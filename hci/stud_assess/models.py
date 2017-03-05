from django.db import models


class Student(models.Model):
    Roll_No = models.CharField(max_length=10)
    Name = models.CharField(max_length=50)
    MQ1 = models.IntegerField()
    MQ2 = models.IntegerField()
    MQ3 = models.IntegerField()
    ML = models.IntegerField()
    EQ1 = models.IntegerField()
    EQ2 = models.IntegerField()
    EQ3 = models.IntegerField()
    EQ4 = models.IntegerField()
    EL = models.IntegerField()
    Assignment = models.FloatField()
    Project = models.FloatField()

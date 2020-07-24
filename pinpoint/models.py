from django.db import models

class Pointset(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    created_by = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Point(models.Model):
    pointset = models.ForeignKey(Pointset, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)
    creation_date = models.DateTimeField('date created')
    created_by = models.CharField(max_length=128)
    def __str__(self):
        return self.name

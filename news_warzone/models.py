from django.db import models

class News(models.Model):

    title = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

class Post(models.Model):
    title = models.CharField(max_length=25)
    data = models.JSONField(null=True, blank=True, default=list)
    time = models.TimeField()
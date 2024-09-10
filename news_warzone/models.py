from django.db import models

class News(models.Model):
    # title - заголовок
    # DateField()
    # TimeField()
    title = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

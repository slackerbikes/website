from django.db import models

class booking(models.Model):
    date = models.DateField(unique=True)
    weekday = models.CharField(max_length=9,unique=False)
    band = models.CharField(max_length=32,unique=False)
    # available = models.BooleanField()

    def __str__(self):
            return str(self.date) if self.date else ''

class gig(models.Model):
    date = models.DateField(unique=True)
    weekday = models.CharField(max_length=9,unique=False)
    band = models.CharField(max_length=32,unique=False)
    # available = models.BooleanField()

    def __str__(self):
            return str(self.date) if self.date else ''
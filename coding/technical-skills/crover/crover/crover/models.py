from django.contrib.postgres.fields import ArrayField
from django.db import models

class graph(models.Model):
    title = models.CharField(max_length=128,unique=True)
    x = models.BinaryField()
    y = models.BinaryField()
    temperature = models.BinaryField()

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Pixels(models.Model):
    color = models.CharField(max_length=100)

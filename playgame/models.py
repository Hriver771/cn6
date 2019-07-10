from django.db import models

# Create your models here.

class Stones(models.Model):
    x1 = models.CharField(max_length = 2)
    y1 = models.IntegerField()
    x2 = models.CharField(max_length = 2)
    y2 = models.IntegerField()
    

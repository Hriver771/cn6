from django.db import models

# Create your models here.

class Stones(models.Model):
    x1 = models.CharField(max_length = 2)
    y1 = models.IntegerField()
    x2 = models.CharField(max_length = 2)
    y2 = models.IntegerField()

    def __str__(self):
        return '%s %s %s %s' % (self.x1, self.y1, self.x2, self.y2)   

 

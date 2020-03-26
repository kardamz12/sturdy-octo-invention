from django.db import models

# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()
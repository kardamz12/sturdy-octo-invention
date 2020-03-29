from django.db import models

# Create your models here.
class Breed(models.Model):
    breed_name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed_name = models.ForeignKey(Breed, default=1, on_delete=models.SET_DEFAULT)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)



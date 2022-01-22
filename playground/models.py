from django.db import models

# Create your models here.
from django.db import models
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Orders(models.Model):
    name = models.CharField(max_length=30)
    cloth = models.CharField(max_length=20)
    size = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    quantity = models.IntegerField()

class Product(models.Model):
    item = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    synonyms = models.CharField(max_length=20)
    image_url= models.URLField()
    image_text = models.CharField(max_length= 20)

class Color(models.Model):
    item = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    synonyms = models.CharField(max_length=20)
    image_url = models.URLField()
    image_text = models.CharField(max_length=20)
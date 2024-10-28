from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField()
    image_source = models.CharField(max_length=20)



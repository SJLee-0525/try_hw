from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=4)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    product = models.ManyToManyField(Product)
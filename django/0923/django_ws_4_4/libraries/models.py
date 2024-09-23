from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField(default=False)
    pubdate = models.DateField()
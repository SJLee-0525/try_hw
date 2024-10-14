from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    name = models.CharField(max_length=100)
    participant = models.ManyToManyField(Participant)
    date = models.DateField()
    location = models.TextField()
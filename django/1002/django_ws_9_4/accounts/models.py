from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
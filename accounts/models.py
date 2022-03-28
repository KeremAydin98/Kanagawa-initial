from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    class Sex(models.TextChoices):
        male = 'M'
        female = 'F'

    email = models.TextField(max_length=254)
    sex = models.CharField(max_length=1, choices=Sex.choices)
    area_code = models.IntegerField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)



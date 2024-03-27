from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choices_role = (('S', 'Seller'),
                    ('M', 'Manager'))
    role = models.CharField(max_length=1, choices= choices_role)


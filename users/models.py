# from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # username, email, password already present
    ROLE_CHOICES = (('user','User'), ('admin','Admin'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    # add phone, address shorthand if needed

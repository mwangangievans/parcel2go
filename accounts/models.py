from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(_("email address"),unique=True)
    phone_number = models.CharField(max_length=50, null=True)
    photo = models.ImageField(null=True)

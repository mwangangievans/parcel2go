from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

PARCEL_CHOICES = (
    ("on_transit", "on_transit"),
    ("delivered", "delivered"),
)


# Create your models here.
class Parcel(models.Model):
    sender = models.ForeignKey(
        User, related_name="parcel_user_sender", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User, related_name="parcel_user_receiver", on_delete=models.CASCADE
    )
    status = models.CharField(max_length=200, choices=PARCEL_CHOICES)

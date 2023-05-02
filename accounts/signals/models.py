import os
from django.db import models
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


# TODO
@receiver(models.signals.post_delete, sender=User)
def auto_delete_photo_on_delete(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=User)
def auto_delete_photo_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_photo = User.objects.get(pk=instance.pk).photo
    except User.DoesNotExist:
        return False
    new_photo = instance.photo
    if not old_photo == new_photo:
        if os.path.isfile(old_photo.path):
            os.remove(old_photo.path)

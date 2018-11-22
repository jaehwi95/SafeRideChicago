from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class nearcrimes(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        location = models.CharField(max_length=50, null=True)
        description = models.TextField()
        date = models.DateTimeField(null=True)
        
class personalcrimes(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        location = models.CharField(max_length=50, null=True)
        description = models.TextField()
        date = models.DateTimeField(null=True)

class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        location = models.CharField(max_length=30, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
                Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


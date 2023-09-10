from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class UserMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    profile_cover = models.ImageField(upload_to='profile_covers/')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_media(sender, instance=None, created=False, **kwargs):
    if created:
        UserMedia.objects.create(
            user = instance,
            profile_pic = "https://static-00.iconduck.com/assets.00/profile-circle-icon-2048x2048-cqe5466q.png",
            profile_cover = "",
        )

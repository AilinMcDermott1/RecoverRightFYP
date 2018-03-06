from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfileModel.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)

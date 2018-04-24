from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from account import models


class Goal(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_data = models.DateTimeField(auto_now_add=False, auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
from django.contrib import admin

# Register your models here.
from account.models import UserProfileModel


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age']

admin.site.register(UserProfileModel, UserProfileAdmin)

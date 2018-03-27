from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify



# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Goal, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# class Post(models.Model):
#     title = models.CharField(max_length=250)
#     body = models.TextField()
#     goal = models.ForeignKey(Goal)
#     slug = models.SlugField(max_length=200, unique=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Post, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title

    # def snippet(self):
    #     return self.body[:50] + '...'
    #
    # def __init__(self):
    #     return self.start_date
    #
    # class Meta:
    #     verbose_name = 'Goal'
    #     verbose_name_plural = 'Goals'
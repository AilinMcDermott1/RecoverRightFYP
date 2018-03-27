from django import forms
from . import models

class CreateGoal(forms.ModelForm):
    class Meta:
        model = models.Goal
        fields = ['title', 'body', 'slug',]
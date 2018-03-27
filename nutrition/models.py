from django.db import models

class savedNutrition(models.Model):
    itemName = models.CharField(max_length=100, default=True)
    valueCalories = models.DecimalField(max_digits=7, decimal_places=2)
    servingUnit = models.CharField(max_length=200, default=True)

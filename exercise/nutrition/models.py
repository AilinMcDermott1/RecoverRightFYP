from django.db import models

class savedNutrition(models.Model):
    itemName = models.CharField(max_length=100, default=True)
    valueCalories = models.DecimalField(max_digits=7, decimal_places=2)
    servingUnit = models.CharField(max_length=200, default=True)

# class Entry(models.Model):
#     entry.value = models.CharField(max_length=10000, default=True)
#     entry.type = models.CharField(max_length=10000, default=True)
#     entry.time = models.DateTimeField(auto_now_add=True, blank=True)

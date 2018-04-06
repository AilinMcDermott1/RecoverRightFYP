from django.conf.urls import url
from . import views
# from nutrition.views import NutritionList

app_name = 'nutrition'

urlpatterns = [
    # url('^nutrition/(?<username>.+)/$', NutritionList.as_view()),
    url('^food/', views.nutritionix, name="nutrition"),
    url('^exercise/', views.exercise, name="exercise"),

]
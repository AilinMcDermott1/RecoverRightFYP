from django.conf.urls import url
from . import views
# from nutrition.views import NutritionList

app_name = 'exercise'

urlpatterns = [
    # url('^nutrition/(?<username>.+)/$', NutritionList.as_view()),
    url('^exercise/', views.exercise, name="exercise"),

]
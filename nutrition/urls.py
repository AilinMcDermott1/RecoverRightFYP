from django.conf.urls import url
from . import views
from .views import ChartView, ChartData, get_data
# from .views import LineChartJSONView


app_name = 'nutrition'

urlpatterns = [
    # url('^nutrition/(?<username>.+)/$', NutritionList.as_view()),
    url('^food/', views.nutritionix, name="nutrition"),
    url('^exercise/', views.exercise, name="exercise"),
    url('^meals/', views.meals, name="meals"),
    url('^chart/$', ChartView.as_view(), name='chart'),
    url('^api/data/$', views.get_data, name="api-data"),
    url('^api/chart/data/$', ChartData.as_view()),

]
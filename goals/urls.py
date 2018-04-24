from django.conf.urls import url
from . import views

app_name = 'goals'
urlpatterns = [
    url(r'^$', views.goal_list, name='goal_list'),
    url(r'^create/$', views.goal_create, name='goal_create'),
    # url(r'^details/$', views.goal_detail, name="goal_detail"),
    # url(r'^delete/$', views.goals_delete, name="goals_delete"),
    url(r'^(?P<id>\d+)/delete/$', views.goals_delete, name='delete'),
    url(r'^(?P<id>\d+)/$', views.goal_detail, name='goal_detail'),

]
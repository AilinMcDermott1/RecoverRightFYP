from django.conf.urls import url
from . import views
from goals.views import GoalListView

app_name = 'goals'

urlpatterns = [
    url(r'^$', views.GoalListView, name="list"),
    # url(r'^$', views=GoalListView.as_view(), name="list"),
    url(r'^create/$', views.goal_create, name="goal_create"),
    url(r'^(?P<slug>[\w-]+)/$', views.goal_detail, name="goal_detail"),
    # url(r'^(?P<slug>.*)/view-goals/', views.goal_detail, name='goal_detail'),
]
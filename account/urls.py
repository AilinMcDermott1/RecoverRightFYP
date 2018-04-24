from django.conf.urls import url

from account import views
from account.views import RegisterUserView, LoginUserView
from django.contrib.auth import views as auth_views


app_name = 'account'
urlpatterns = [
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    url(r'^login/$', view=LoginUserView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'account:login'}, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.update_profile, name='edit_profile'),

]
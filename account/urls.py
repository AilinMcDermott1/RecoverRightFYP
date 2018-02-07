from django.conf.urls import url

from account import views
from account.views import RegisterUserView, LoginUserView

urlpatterns = [
    #/account/register
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    url(r'^login/$', view=LoginUserView.as_view(), name='login'),
    url(r'^profile/$', views.profile, name='profile'),
]
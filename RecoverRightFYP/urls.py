
from django.conf.urls import url, include
from django.contrib import admin
from RecoverRightFYP import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^account/', include("account.urls")),
    url(r'^admin/', admin.site.urls),
]

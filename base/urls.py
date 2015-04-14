from django.conf.urls import url
#from django.contrib.auth import login, logout
from . import views

urlpatterns = [
    url(r'^$', views.base),
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
]


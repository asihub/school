from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.library),
    #url(r'^saved/$', views.saved),
]


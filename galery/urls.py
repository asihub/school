from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.galery),
    url(r'^(?P<album_id>\d+)/$', views.album),
]


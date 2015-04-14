from django.conf.urls import url

from . import views

urlpatterns = [    
    url(r'^$', views.yearCalend),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', views.yearCalend),
]


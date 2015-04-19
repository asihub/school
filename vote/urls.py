from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.votes),
    url(r'^(?P<vote_id>\d+)/$', views.vote),
]


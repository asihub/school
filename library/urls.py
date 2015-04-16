from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.library),
    url(r'^(?P<lib_id>\d+)/$', views.books),
    #url(r'^saved/$', views.saved),
]


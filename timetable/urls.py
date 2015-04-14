from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.timetable),
    url(r'^(?P<week>next)/$', views.timetable),
    url(r'^(?P<week>this)/$', views.timetable),

]


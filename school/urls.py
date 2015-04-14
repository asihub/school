from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'school.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('base.urls')),
    url(r'^base/', include('base.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^timetable/', include('timetable.urls')),
    url(r'^lib/', include('library.urls')),
    url(r'^diary/', include('diary.urls')),
    url(r'^calend/', include('calend.urls')),
    url(r'^forum/', include('forum.urls')),
]

from django.conf.urls import patterns, url
from gallery import views

urlpatterns = patterns('',
    url(r'^', views.home, name='home'),
    url(r'^(?P<album_id>\d+)/$', views.album, name='album'),
)

from django.conf.urls import patterns, url
from persons import views

urlpatterns = patterns('',
    url(r'^login/', views.loginuser, name='login'),
    url(r'^register/', views.registeruser, name='register'),
    url(r'^promoter/', views.registerpromoter, name='promoter'),
    url(r'^logout/', views.logoutuser, name='logout'),
    url(r'^profile/', views.profile, name='profile'),
)

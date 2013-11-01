from django.conf.urls import patterns, url
from persons import views

urlpatterns = patterns('',
    url(r'^login/', views.loginuser, name='login'),
    url(r'^register/', views.registeruser, name='register'),
    url(r'^register_promoter/', views.registerpromoter, name='registerprom'),
    url(r'^logout/', views.logoutuser, name='logout'),
)

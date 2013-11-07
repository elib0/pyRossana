from django.conf.urls import patterns, url
from persons import views

urlpatterns = patterns('',
    url(r'^login/', views.loginuser, name='login'),
    url(r'^register/', views.registeruser, name='register'),
    url(r'^prom/', views.registerpromoter, name='prom'),
    url(r'^promoter/', views.ajax_register_promoter, name='promoter'),
    url(r'^logout/', views.logoutuser, name='logout'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^profile/save', views.ajax_update_profile, name='save_profile'),

)

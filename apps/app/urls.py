from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.index),
        url(r'^register$',views.register),
        url(r'^login$',views.login),
        url(r'^home$',views.home),
        url(r'^logout$', views.logout),
        url(r'^show/(?P<id>\d+)$', views.show),
        url(r'^show_other/(?P<id>\d+)$', views.show_other),
        url(r'^add_friend/(?P<id>\d+)$', views.add_friend),
        url(r'^remove_friend/(?P<id>\d+)$', views.remove_friend),
    ]
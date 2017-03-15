from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sum/(?P<x>\d+)/$', views.mysum),
]


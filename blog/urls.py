from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^archives/$', views.archives),
    url(r'^new/$', views.post_new, name='post_new'),
]

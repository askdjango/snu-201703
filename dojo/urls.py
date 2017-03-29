from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^flower.jpg$', views.image_download),
    url(r'^json_response/$', views.json_response),
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]{2,4})/(?P<age>\d{1,3})/$', views.hello),
    url(r'^(?P<name>[ㄱ-힣]{2,4}).png$', views.nametag),
]


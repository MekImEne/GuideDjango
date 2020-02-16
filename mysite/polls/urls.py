from django.conf.urls import url
from . import views

urlpatterns= {
    url(r'^$', views.index, name="index"), #we cant add anything to the URL 127.0.0.1/polls

}
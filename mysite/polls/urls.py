from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns= [
    url(r'^$', views.index, name="index"), #we cant add anything to the URL 127.0.0.1/polls
    url(r'^(?P<question_id>[0-9]+)/$', views.detail , name="detail"), #127.0.0.1/polls/1 (question_id)
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),  # 127.0.0.1/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),  # 127.0.0.1/polls/1/vote

]
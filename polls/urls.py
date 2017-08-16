from django.conf import settings
from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.CreatePoll.as_view(), name='poll'),
    url(r'^gracias/$', views.thanks, name='thanks'),
]

from django.conf import settings
from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    # Diners pin
    url(r'^$', views.poll, name='poll'),
]

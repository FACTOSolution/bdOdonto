from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^odontograma$', views.odontograma, name='odontograma'),
]


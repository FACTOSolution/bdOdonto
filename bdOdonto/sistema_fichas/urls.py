from django.conf.urls import url
from . import views

app_name = 'bdodonto'
urlpatterns = [
    url(r'^odontograma/$', views.odontograma, name='index-view'),
]

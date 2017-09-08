from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

app_name = 'sistema_fichas'
urlpatterns = [
    url(r'^odontograma/$', views.odontograma, name='index-view'),
	url(r'^index/$', views.index),
]

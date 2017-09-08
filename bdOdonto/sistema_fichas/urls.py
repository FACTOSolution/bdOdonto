from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

app_name = 'bdodonto'
urlpatterns = [
    url(r'^odontograma/$', views.odontograma, name='index-view'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ver_animal, name = 'ver_animal'),
	url(r'^crearanimal/$', views.crearanimal, name = 'crearanimal'),
]
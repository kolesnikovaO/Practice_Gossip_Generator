from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
	url(r'^$', views.statistic, name='Stat')
]

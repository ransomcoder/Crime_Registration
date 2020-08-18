from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^new/', views.new, name='new'),
    url(r'^services/', views.services, name='services'),
    path('', views.submit, name='submit'),
]
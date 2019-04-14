from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'shorturl'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('redirect/<code>', views.redirect, name='redirect')
]
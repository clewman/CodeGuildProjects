from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'bibliothek'
urlpatterns = [
    path('', views.index, name='index'),
    path('check_book/', views.check_book, name='check_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('check_author/', views.check_author, name='check_author'),
    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('checkout/', views.checkout, name='checkout')
]
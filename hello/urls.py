from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.hello_there, name='hello_there'),
    path('account', views.account, name='account'),
    path('subjects', views.subjects, name='subjects'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('user', views.user, name='user'),
]

url(r'^connexion$', views.connexion, name='connexion'),
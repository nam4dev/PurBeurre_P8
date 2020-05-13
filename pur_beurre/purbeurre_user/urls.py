from django.urls import path
from . import views

urlpatterns = [
    path(r'^connection$', views.connection, name='connection'),
    path(r'^disconnection$', views.disconnection, name='disconnection'),
    path(r'^create_account$', views.create_account, name='create_account'),
    path(r'^my_account$', views.my_account, name='my_account'),

]

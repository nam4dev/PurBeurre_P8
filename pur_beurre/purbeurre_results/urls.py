from django.urls import path
from . import views

urlpatterns = [
    path('results', views.results, name='results'),
    path('detail/<int:product_id>', views.detail, name='detail'),
]

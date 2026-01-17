from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.rozwiaz_test, name='test_auto'),
]
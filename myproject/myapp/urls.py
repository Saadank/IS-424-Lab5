from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_view, name='add'),
    path('', views.default_view, name='default'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.loby, name="loby"),
    path('<str:room_name>/', views.room_name, name="room_name"),
]

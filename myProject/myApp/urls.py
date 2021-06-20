from django.urls import path, include
from . import views
urlpatterns = [
    path('user-form/', views.insertData, name="insertData"),
    path('allusers/', views.allusers, name="allusers"),
]
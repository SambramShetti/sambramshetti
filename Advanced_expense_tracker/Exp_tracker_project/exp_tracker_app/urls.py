from django.contrib import admin
from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.home, name='home'),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("delete/<int:id>/", views.delete, name="delete")
]
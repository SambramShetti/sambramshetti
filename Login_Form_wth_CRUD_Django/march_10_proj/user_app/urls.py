from django.contrib import admin
from django.urls import path
from . import views
# from .views import CustomLoginView
from django.contrib.auth import views as authentication_views


urlpatterns = [
path('register/', views.register, name='register'),
path('login/', authentication_views.LoginView.as_view(template_name = 'user_app/login.html'), name='login'),
path('profile/', views.profilepage, name='profile'),
path('logout/', authentication_views.LogoutView.as_view(template_name='user_app/logout.html'), name='logout')
]
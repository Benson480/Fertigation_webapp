from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('elements/', views.elements, name='elements'),
    path('template/', views.template, name='template'),
    path('index/', views.template, name='index'),
    path('members/details/elements/', views.elements, name='elements'),
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Fertilizers/', views.Fertilizers, name='Fertilizers'),
    path('Fertilizers/<int:id>', views.Fertilizers, name='details'),
    path('testing/', views.testing, name='testing'),
    path('elements/', views.elements, name='elements'),
    path('ppm/', views.ppm, name='ppm'),
    path('template/', views.template, name='template'),
    path('index/', views.index, name='index'),
    path('Fertilizers/delete/<int:id>', views.delete, name='delete'),
    path('Fertilizers/deleteprice/<int:id>', views.deleteprice, name='deleteprice'),
    path('Fertilizers/elements/', views.elements, name='elements'),
    path('Fertilizers/update/<int:id>', views.update, name='update'),
    path('Fertilizers/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('about/', views.about, name='about'),
    path('anouncement/', views.anouncement, name='anouncement'),
    path('contacts/', views.contacts, name='contacts'),
    path('prices/', views.prices, name='prices'),
    path('weather/', views.weather, name='index'),
    path('Fertlizer_dealers/', views.Fertlizer_dealers, name='Fertlizer_dealers'),
    path('laboratory/', views.laboratory, name='laboratory'),
    path('research/', views.research, name='research'),
    
]
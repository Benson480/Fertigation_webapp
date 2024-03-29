from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)

urlpatterns = [
    path('login/', views.login_view, name='login'),
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
    path('ppm/delete_ppm/<int:id>', views.delete_ppm, name='delete_ppm'),
    path('delete_fertilizers/<int:id>', views.delete_fertilizers, name='delete_fertilizers'),
    path('deleteimages/<int:id>', views.deleteimages, name='deleteimages'),
    path('deleteprice/<int:id>', views.deleteprice, name='deleteprice'),
    path('elements/delete_elements/<int:id>', views.delete_elements, name='delete_elements'),
    path('fertilizer_list/delete/<int:id>', views.delete, name='delete'),
    path('Fertilizers_recycle/delete_fertilizers_recycle/<int:id>', views.delete_fertilizers_recycle, name='delete_recycle'),
    path('Fertilizers/deleteprice/<int:id>', views.deleteprice, name='deleteprice'),
    path('Fertilizers/elements/', views.elements, name='elements'),
    path('Fertilizers/update/<int:id>', views.update, name='update'),
    path('Fertilizers/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('fertilizer_list/update_list/UpdateFertilizerList/<int:id>', views.UpdateFertilizerList, name='UpdateFertilizerList'),
    path('about/', views.about, name='about'),
    path('anouncement/', views.anouncement, name='anouncement'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact/', views.contact, name='contact'),
    path('prices/', views.prices, name='prices'),
    path('weather/', views.weather, name='index'),
    path('Fertlizer_dealers/', views.Fertlizer_dealers, name='Fertlizer_dealers'),
    path('laboratory/', views.laboratory, name='laboratory'),
    path('research/', views.research, name='research'),
    path('fertilizer_list/', views.fertilizer_list, name='fertilizer_list'),
    path('regenerate_csrf_token/', views.regenerate_csrf_token, name='regenerate_csrf_token'),
    path('delete_multiple/', views.delete_multiple_items, name='delete_multiple_items'),
    path('delete_multiple_fertilizers/', views.delete_multiple_fertilizers, name='delete_multiple_fertilizers'),
    path('upload/', views.upload_image, name='upload_image'),
    path('diagnosis/', views.image_list, name='image_list'),
    path('Fertilizers_recycle/', views.UvElements, name='Fertilizers_recycle'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
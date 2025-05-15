from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registro/', views.registro, name='registro'),
    path('libros/', views.libros, name='libros'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
    path('single-audio/', views.single, name='single'),
    path('single-standard/', views.single_s, name='single_s'),
    path('single-video/', views.single_vi, name='single_vi'),
    path('styles/', views.styles, name='styles'),
    ]
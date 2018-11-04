from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


urlpatterns = [
    path('', views.user_login, name='login'),
    path('register', views.user_register, name='register'),
    path('home', views.index, name='index'),
    path('form', views.addForm, name = 'form'),
    path('staffs', views.staff, name='staffs'),
    path('search', views.search, name='search'),
    path('profile/<int:staffs_id>/', views.profile, name='profile'),
    path('Nform', views.n_addForm, name = 'Nform'),
    path('Nstaffs', views.n_staff, name = 'Nstaffs'),
    path('favicon.ico', lambda x: HttpResponseRedirect(settings.STATIC_URL+'images/favicon.ico')),
]
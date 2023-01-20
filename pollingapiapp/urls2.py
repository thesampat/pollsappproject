from .views2 import *
from django.shortcuts import render, redirect
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', view=home, name='home'),
    path('login', view=login, name='login'),
    path('profile', view=profile, name='profile'),
    path('register', view=register, name='register'),
    path('create', view=createPoll, name='cretePoll'),
    path('login_user', view=login_user, name='loginUser'),
    path('register_user', view=register_user, name='register'),
    path('logout_user', view=logout_user, name='logout'),
    path('create_poll', view=create_poll, name='create_poll'),
    path('register_user_api', view=register_user_api, name='register'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

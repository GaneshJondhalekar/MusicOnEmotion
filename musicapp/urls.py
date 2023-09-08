"""Emusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('accounts',views.accounts,name='accounts'),
    path('Profile', views.profile,name='Profile'),
    path('RecentlyPlayed', views.recentlyPlayed),
    path('Favourite', views.favourite),
    path('Playlist', views.playlist,name='playlist'),
    path('Capture',views.capture),
    path('Detect',views.detect),
    path('Songs/<int:id>',views.songs,name='Songs'),
    path('search',views.search),
    path('play/<int:id>',views.play,name='play'),
]

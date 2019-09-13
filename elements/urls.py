from django.contrib import admin
from django.urls import path, include
from elements import views

urlpatterns = [
    path('', views.scrape, name='scrape'),
]
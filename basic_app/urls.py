"""This file is for inter-app routing"""
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

# interapp routing
urlpatterns = [
    # Method for returning a class-based-view
    path('', views.CBView.as_view(), name="index"),
]
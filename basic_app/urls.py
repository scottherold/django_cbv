"""This file is for inter-app routing"""
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

# interapp routing
urlpatterns = [
    # Method for returning a class-based-view
    path('', views.IndexView.as_view(), name="index"),
    path('list', views.SchoolListView.as_view(), name='list'),
    # <int:pk> creates a path variable called pk to send to the
    # SchoolDetailView
    path('<int:pk>', views.SchoolDetailView.as_view(), name='detail'),
    path('create', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='delete')
]
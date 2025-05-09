from django.urls import path
from . import views  # Ensure you have a views.py

urlpatterns = [
    path('', views.api_list, name='project_list'),  # or any valid view
]

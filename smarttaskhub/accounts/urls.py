from django.urls import path
from . import views  # make sure views.py exists in the same folder

urlpatterns = [
    path('login/', views.login_view, name='login'),  # or any valid view
    path('logout/', views.logout_view, name='logout'),  # or any valid view
    path('register/', views.register_view, name='register'),  # or any valid view
    path('home/', views.home_view, name='home'),  # or any valid view
]

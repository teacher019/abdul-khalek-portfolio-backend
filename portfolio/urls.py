
from django.urls import path
from .views import profile_api, projects_api

urlpatterns = [
    path('profile/', profile_api, name='profile-api'),
    path('projects/', projects_api, name='projects-api'),
]

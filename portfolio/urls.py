
from django.urls import path
from .views import profile_api, projects_api, project_detail_api

urlpatterns = [
    path('profile/', profile_api, name='profile-api'),
    path('projects/', projects_api, name='projects-api'),
    path('projects/<int:pk>/', project_detail_api, name='project-detail-api'),
]

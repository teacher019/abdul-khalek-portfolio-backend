from django.urls import path

from .views import (
    profile_api,
    projects_api,
    project_detail_api,
    blog_posts_api,
    blog_post_detail_api,
    blog_comments_api,
    contact_message_api,
)

urlpatterns = [
    path("contact/", contact_message_api, name="contact-message-api"),
    path("profile/", profile_api, name="profile-api"),
    path("projects/", projects_api, name="projects-api"),
    path(
        "projects/<int:pk>/",
        project_detail_api,
        name="project-detail-api",
    ),
    path("blog/", blog_posts_api, name="blog-posts-api"),
    path(
        "blog/<slug:slug>/",
        blog_post_detail_api,
        name="blog-post-detail-api",
    ),
    path(
        "blog/<slug:slug>/comments/",
        blog_comments_api,
        name="blog-comments-api",
    ),
]

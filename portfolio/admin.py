
from django.contrib import admin
from .models import Project, BlogPost, BlogComment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "description", "category")
    ordering = ("id",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "published",
        "created_at",
    )
    list_filter = ("published", "category", "created_at")
    search_fields = ("title", "excerpt", "content", "slug")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("published",)
    ordering = ("-created_at",)


@admin.action(description="Approve selected comments")
def approve_comments(modeladmin, request, queryset):
    queryset.update(approved=True)


@admin.action(description="Unapprove selected comments")
def unapprove_comments(modeladmin, request, queryset):
    queryset.update(approved=False)


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "post",
        "approved",
        "created_at",
    )
    list_filter = ("approved", "created_at")
    search_fields = ("name", "email", "message", "post__title")
    list_editable = ("approved",)
    actions = [approve_comments, unapprove_comments]
    ordering = ("-created_at",)

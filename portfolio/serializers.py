
from rest_framework import serializers

from .models import Project, BlogPost, BlogComment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "category",
            "description",
            "technologies",
            "github_url",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "excerpt",
            "content",
            "published",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = [
            "id",
            "post",
            "name",
            "email",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_post(self, post):
        if not post.published:
            raise serializers.ValidationError(
                "Comments can only be added to published posts."
            )
        return post

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Name is required.")
        return value

    def validate_message(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Comment cannot be empty.")
        return value

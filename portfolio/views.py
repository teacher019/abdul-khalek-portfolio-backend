from django.db.models import Q, Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Project,
    BlogPost,
    BlogComment,
    ContactMessage,
    BlogLike,
)
from .serializers import (
    ProjectSerializer,
    BlogPostSerializer,
    BlogCommentSerializer,
    ContactMessageSerializer,
)


@api_view(["GET"])
def profile_api(request):
    profile = {
        "name": "Abdul Khalek",
        "title": "Mathematics & Physics Teacher | Web & App Developer",
        "location": "Bangladesh",
        "teaching_experience": "37+ years",
        "skills": [
            "Mathematics", "Physics", "Python", "Django",
            "React", "WordPress", "Flutter", "JavaScript",
        ],
        "interests": [
            "Full Stack Web Development",
            "Mobile App Development",
            "Artificial Intelligence",
        ],
    }
    return Response(profile)


@api_view(["GET"])
def projects_api(request):
    serializer = ProjectSerializer(Project.objects.all(), many=True)
    return Response(serializer.data)


@api_view(["GET"])
def project_detail_api(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return Response(ProjectSerializer(project).data)


@api_view(["GET"])
def blog_posts_api(request):
    posts = BlogPost.objects.filter(published=True).annotate(
    like_count=Count("likes")
    )
    search_query = request.query_params.get("search", "").strip()
    category = request.query_params.get("category", "").strip()

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query)
            | Q(excerpt__icontains=search_query)
            | Q(content__icontains=search_query)
        )

    if category:
        posts = posts.filter(category__iexact=category)

    return Response(BlogPostSerializer(posts, many=True).data)


@api_view(["GET"])
def blog_post_detail_api(request, slug):
    post = get_object_or_404(
        BlogPost.objects.annotate(like_count=Count("likes")),
        slug=slug,
        published=True,
    )
    return Response(BlogPostSerializer(post).data)

@api_view(["GET", "POST"])
def blog_comments_api(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)

    if request.method == "GET":
        comments = BlogComment.objects.filter(
            post=post,
            approved=True,
        )
        serializer = BlogCommentSerializer(comments, many=True)
        return Response(serializer.data)

    serializer = BlogCommentSerializer(
        data={**request.data, "post": post.pk}
    )
    if serializer.is_valid():
        serializer.save(approved=False)
        return Response(
            {
                "message": "Comment submitted for moderation.",
                "comment": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def contact_message_api(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Your message has been received."},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
def blog_like_api(request, slug):
    post = get_object_or_404(
        BlogPost,
        slug=slug,
        published=True,
    )

    visitor_id = request.data.get("visitor_id", "")
    visitor_id = str(visitor_id).strip()

    if not visitor_id or len(visitor_id) > 64:
        return Response(
            {
                "error": "A valid visitor_id is required."
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    like, created = BlogLike.objects.get_or_create(
        post=post,
        visitor_id=visitor_id,
    )

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    like_count = BlogLike.objects.filter(post=post).count()

    return Response(
        {
            "liked": liked,
            "like_count": like_count,
        },
        status=status.HTTP_200_OK,
    )

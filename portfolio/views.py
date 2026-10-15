from .models import Project
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def profile_api(request):
    profile = {
        "name": "Abdul Khalek",
        "title": "Mathematics & Physics Teacher | Web & App Developer",
        "location": "Bangladesh",
        "teaching_experience": "37+ years",
        "skills": [
            "Mathematics",
            "Physics",
            "Python",
            "Django",
            "React",
            "WordPress",
            "Flutter",
            "JavaScript",
        ],
        "interests": [
            "Full Stack Web Development",
            "Mobile App Development",
            "Artificial Intelligence",
        ],
    }

    return Response(profile)

@api_view(['GET'])
def projects_api(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def project_detail_api(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

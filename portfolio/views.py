
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
    projects = [
        {
            "id": 1,
            "title": "React Shopping Cart",
            "category": "Frontend Development",
            "description": "A responsive shopping cart with product details, quantity controls, cart management, and localStorage.",
            "technologies": ["React", "JavaScript", "CSS", "Vite"],
            "github_url": "https://github.com/teacher019",
        },
        {
            "id": 2,
            "title": "Live Score App",
            "category": "Flutter App Development",
            "description": "A mobile application project using Firebase services and Flutter.",
            "technologies": ["Flutter", "Dart", "Firebase"],
            "github_url": "https://github.com/teacher019/live_score_project_app",
        },
        {
            "id": 3,
            "title": "Attendance Tracker",
            "category": "Flutter App Development",
            "description": "A student attendance tracking project using Provider and ChangeNotifier.",
            "technologies": ["Flutter", "Dart", "Provider"],
            "github_url": "https://github.com/teacher019/student_record_assignment",
        },
        {
            "id": 4,
            "title": "Multi-Author Blog",
            "category": "Backend Development",
            "description": "A Django blog project with features including search, pagination, comments, and likes.",
            "technologies": ["Python", "Django", "SQLite"],
            "github_url": "https://github.com/teacher019",
        },
    ]

    return Response(projects)

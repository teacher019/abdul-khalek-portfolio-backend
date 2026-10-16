
from django.db import migrations


PROJECTS = [
    {
        "title": "React Shopping Cart",
        "category": "Frontend Development",
        "description": "A responsive shopping cart with product details, quantity controls, cart management, and localStorage.",
        "technologies": ["React", "JavaScript", "CSS", "Vite"],
        "github_url": "https://github.com/teacher019/React-Shopping-Cart-project",
    },
    {
        "title": "Live Score App",
        "category": "Flutter App Development",
        "description": "A mobile application project using Firebase services and Flutter.",
        "technologies": ["Flutter", "Dart", "Firebase"],
        "github_url": "https://github.com/teacher019/live_score_project_app",
    },
    {
        "title": "Attendance Tracker",
        "category": "Flutter App Development",
        "description": "A student attendance tracking project using Provider and ChangeNotifier.",
        "technologies": ["Flutter", "Dart", "Provider"],
        "github_url": "https://github.com/teacher019/student_record_assignment",
    },
    {
        "title": "Multi-Author Blog",
        "category": "Backend Development",
        "description": "A Django blog project with search, pagination, comments, and likes.",
        "technologies": ["Python", "Django", "SQLite"],
        "github_url": "https://github.com/teacher019",
    },
]


def seed_projects(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    database = schema_editor.connection.alias

    for item in PROJECTS:
        Project.objects.using(database).get_or_create(
            title=item["title"],
            defaults={
                "category": item["category"],
                "description": item["description"],
                "technologies": item["technologies"],
                "github_url": item["github_url"],
            },
        )


def unseed_projects(apps, schema_editor):
    # Intentionally preserve project data when reversing this migration.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_projects, unseed_projects),
    ]

import requests
from django.shortcuts import render
from gallery.models import Project

def home(request):
    projects = Project.objects.all().order_by('order')
    username = "luiscazares"
    url = f"https://api.github.com/users/{username}/events/public"

    github_data = []
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            github_data = response.json()[:5]
    except requests.exceptions.RequestException:
        github_data = []
    
    context = {
        'events': github_data,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)
import requests
from django.shortcuts import render

def home(request):
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
        'events': github_data
    }
    return render(request, 'portfolio/home.html')
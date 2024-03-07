
from django.shortcuts import render
from .models import UserProfile, Lesson, Language, UserLanguage, CommunityPost
from django.contrib.auth.views import LoginView
from .models import Lesson
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import UserProfile
def index(request):
  
    return render(request, 'index.html')

def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_languages = UserLanguage.objects.filter(user=request.user)
    community_posts = CommunityPost.objects.all()
    
    # Fetch completed lessons and favorite language
    completed_lessons = user_profile.completed_lessons.all()
    favorite_language = user_profile.favorite_language

    context = {
        'user_profile': user_profile,
        'user_languages': user_languages,
        'community_posts': community_posts,
        'completed_lessons': completed_lessons,
        'favorite_language': favorite_language,
    }

    return render(request, 'dashboard.html', context)
def community_posts(request):
    posts = CommunityPost.objects.all()
    return render(request, 'community_posts.html', {'posts': posts})

def create_community_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        CommunityPost.objects.create(user=user, title=title, content=content)
        return redirect('community_posts')
    return render(request, 'create_community_post.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Fix here
            # return redirect('dashboard')  # Redirect to the dashboard or desired page
            return render(request, 'login.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# language_app/views.py
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or another page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# language_app/views.py


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    
    # Track user progress
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.completed_lessons.add(lesson)

    return render(request, 'lesson_detail.html', {'lesson': lesson})


from django.shortcuts import render
from .models import UserProfile, Lesson, Language, UserLanguage, CommunityPost
from django.contrib.auth.views import LoginView
from .models import Lesson
from .forms import FavoriteLanguageForm,LessonTagForm,LanguageForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from django.urls import reverse

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

from .forms import UserProfileForm


def update_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after successful form submission
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
    }

    return render(request, 'update_profile.html', context)
from .forms import LessonForm

def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            return redirect('update_profile')# Redirect to the lesson detail page after successful form submission
            
    else:
        form = LessonForm()

    context = {
        'form': form,
    }

    return render(request, 'create_lesson.html', context)
def create_community_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        CommunityPost.objects.create(user=user, title=title, content=content)
        return redirect('community_posts')
    return render(request, 'create_community_post.html')
from .forms import FavoriteLanguageForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
def index(request):
    return render(request,"index.html")

        
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
              auth.login(request,user)
              return render (request,'dashboard.html')
        else:
            messages.info(request,"successfully")
            #data=user.objects.all()
            #return render(request,'home.html',{'da':data})
            return render(request,'login.html')
    else:    
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    messages.success(request,"logout succesfully")
    return render(request,"index.html")
        

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import UserProfile
def login(request):
    if request.method == 'POST':

        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            user_profile = UserProfile.objects.get(user=user)
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def signup(request):
    """
    signup user
    input: user_type,user_name,password,phone number
    """
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                if user:
                    messages.error(request, 'Username already exists!')
                    return render(request, 'signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'],
                    first_name=request.POST['name'],
                    email=request.POST['email'])
                    
                auth.login(request, user)
                user_profile = UserProfile.objects.create(
                    user=request.user)
                user_profile.fullName = request.POST['name']
                user_profile.Email= request.POST['email']
                print(request.FILES)
                user_profile.save()
                return redirect('dashboard')
        else:
            messages.error(request, 'Passwords should match')
            return render(request, 'signup.html')
    return render(request, 'signup.html')


def logout(request):
    """
    logout user
    """
    if request.method == "POST":
        auth.logout(request)
        return render(request, 'login.html')
    auth.logout(request)
    return render(request, 'login.html')

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    
    # Track user progress
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.completed_lessons.add(lesson)

    return render(request, 'lesson_detail.html', {'lesson': lesson})
def create_lesson_tag(request):
    if request.method == 'POST':
        form = LessonTagForm(request.POST)
        if form.is_valid():
            lesson_tag = form.save()
            return redirect('create_lesson')  # Redirect to the lesson_tags page after successful form submission
    else:
        form = LessonTagForm()

    context = {
        'form': form,
    }

    return render(request, 'create_lesson_tag.html', context)
def language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save()
            return redirect('dashboard')  # Redirect to the lesson_tags page after successful form submission
    else:
        form = LanguageForm()

    context = {
        'form': form,
    }

    return render(request, 'language.html', context)

from .forms import FavoriteLanguageForm

def select_favorite_language(request):
    if request.method == 'POST':
        form = FavoriteLanguageForm(request.POST)
        if form.is_valid():
            user_language = form.save(commit=False)
            user_language.user = request.user
            user_language.save()
            return redirect('index')  # Redirect to the index page after successful form submission
    else:
        form = FavoriteLanguageForm()

    context = {
        'form': form,
    }

    return render(request, 'select_favorite_language.html', context)



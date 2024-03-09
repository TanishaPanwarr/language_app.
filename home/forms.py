# language_app/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from django.db.models import fields 
from .models import UserProfile,Lesson,Language,LessonTag,UserLanguage
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
# language_app/forms.py
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # You can customize the form if needed (e.g., add extra fields, widgets, etc.)
    class Meta:
        model = User  # Assuming User model is imported
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fullName', 'language_level', 'completed_lessons', 'favorite_language']
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'difficulty', 'tags']

    # You can customize the form further based on your requirements
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the lesson title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the lesson content'}))

    # You can add custom validation or widgets if needed
    # For example, you can use a dropdown list for difficulty selection
    difficulty = forms.ChoiceField(choices=Lesson.difficulty_choices)
    tags = forms.ModelMultipleChoiceField(queryset=LessonTag.objects.all(), widget=forms.CheckboxSelectMultiple)
class LanguageForm(forms.ModelForm):
    class Meta:
        model = UserLanguage
        fields = ['language','user']
       
class FavoriteLanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']
       
from .models import LessonTag

class LessonTagForm(forms.ModelForm):
    class Meta:
        model = LessonTag
        fields = ['name']

    # You can add custom validation or widgets if needed
    # For example, you can add a placeholder to the name field
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter tag name'}))
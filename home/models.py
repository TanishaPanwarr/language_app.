# language_app/models.py

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=100,default="")
    Email=models.EmailField(max_length=100)
    language_level_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    language_level = models.CharField(max_length=20, choices=language_level_choices)
    
    # New fields for progress tracking and personalization
    completed_lessons = models.ManyToManyField('Lesson', blank=True, related_name='completed_by_users')
    favorite_language = models.ForeignKey('Language', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    difficulty_choices = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = models.CharField(max_length=20, choices=difficulty_choices)
    created_at = models.DateTimeField(auto_now_add=True)
  
    
    # New field for tags or categories
    tags = models.ManyToManyField('LessonTag', blank=True)
    def __str__(self):
        return self.title

class LessonTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.language.name}"

class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

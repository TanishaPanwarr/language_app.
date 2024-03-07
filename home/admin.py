# language_app/admin.py

from django.contrib import admin
from .models import UserProfile, Lesson, Language, UserLanguage, CommunityPost, LessonTag

admin.site.register(UserProfile)
admin.site.register(Lesson)
admin.site.register(Language)
admin.site.register(UserLanguage)
admin.site.register(CommunityPost)
admin.site.register(LessonTag)

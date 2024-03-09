
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('UserProfile/',views.UserProfile, name='Userprofile'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('community/',views.community_posts, name='community_posts'),
    path('community/create/',views.create_community_post, name='create_community_post'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('create_lesson/', views.create_lesson, name='create_lesson'),
    path('select_favorite_language/',views.select_favorite_language, name='select_favorite_language'),
    path('create_lesson_tag/', views.create_lesson_tag, name='create_lesson_tag'),
    path('language/', views.language, name='language'),
]



from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('community/',views.community_posts, name='community_posts'),
    path('community/create/',views.create_community_post, name='create_community_post'),


]


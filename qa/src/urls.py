from django.urls import path
from src import views

urlpatterns = [
    path('registration/', views.registration, name='registr'),
    path('authorization/', views.authorization, name='auth'),
    path('', views.index, name='home'),
    path('logout/', views.exit, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.posts, name='posts'),
    path('chat/', views.chat, name='chat'),
    path('search/', views.search, name='search'),
]
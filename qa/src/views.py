from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q

from datetime import timedelta, date
from src import models

import datetime


def index(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(reverse('auth'))

    if request.user.is_authenticated:
        context = {'title': 'Home'}
        return render(request, 'src/index.html', context=context)

def registration(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect(reverse('posts'))

    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            login(user=user, request=request)
            return redirect(reverse('posts'))
        # print(request.POST)
        # print(request.FILES)
        # if request.POST.get('password') == request.POST.get('password_c'):
        #     user = models.User(username=request.POST.get('username'))
        #     user.set_password(request.POST.get('password'))
        #     user.save()
            
        #     mother = models.Mother(user=user, first_name=request.POST.get('first_name'),
        #     last_name=request.POST.get('last_name'), weight=request.POST.get('weight'),
        #     height=request.POST.get('height'), gestation_date=request.POST.get('gestation_date'),
        #     phone_number=request.POST.get('phone_number'), city=request.POST.get('city'),
        #     children_count=request.POST.get('children_count'), photo=request.POST.get('photo'), 
        #     birth_date=request.POST.get('photo'))
    
    context = {'title': 'Регистрация'}

    return render(request, 'src/registration.html', context=context)


def authorization(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect(reverse('posts'))
    
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))

        if user is not None:
            login(user=user, request=request)
            return redirect(reverse('posts'))

    context = {'title': 'Авторизация'}

    return render(request, 'src/authorization.html', context=context)


def exit(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(reverse('auth'))

    logout(request)

    return redirect(reverse('auth'))    


def profile(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(reverse('auth'))
    
    if request.method == 'GET':
        mother = models.Mother.objects.get(user=request.user)
        mother.gestation_date = (date.today() - mother.gestation_date).days // 7
        mother.birth_date = (date.today() - mother.birth_date).days // 365
        posts = models.Post.objects.filter(author=mother)
        print(posts)

        context = {'title': 'Профиль', 'mother': mother, 'posts': posts}

        return render(request, 'src/profile.html', context=context)


def posts(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(reverse('auth'))
    
    if request.method == 'GET':
        mother = models.Mother.objects.get(user=request.user)
        posts = models.Post.objects.all()
        context = {'title': 'Публикации', 'posts': posts}

        return render(request, 'src/posts.html', context=context)

def chat(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(reverse('auth'))
    
    if request.method == 'GET':
        context = {'title': 'Чат'}

        return render(request, 'src/chat.html', context=context)


def search(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect(reverse('auth'))
    
    if request.method == 'GET':
        mothers = models.Mother.objects.filter(~Q(user=request.user)).all()
        context = {'title': 'Поиск', 'mothers': mothers}

        return render(request, 'src/search.html', context=context)

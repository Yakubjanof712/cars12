from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Car, Comment
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, "Royxatdan  otdingiz!")
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'car/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Tizimga  kirdingiz!")
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'car/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "Tizimdan  chiqdingiz!")
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    cars = Car.objects.all()
    return render(request, 'car/dashboard.html', {'cars': cars})


@login_required(login_url='login')
def add_comment(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.user = request.user
            comment.save()
            messages.success(request, "Izoh  qoshildi!")
            return redirect('dashboard')
    else:
        form = CommentForm()
    return render(request, 'car/comment_form.html', {'form': form, 'car': car})
